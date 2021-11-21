import json, re

from django.views import View
from django.http  import JsonResponse
from django.core.exceptions import ValidationError

from users.models import User

class SignupView(View):

    def post(self, request):

        data = json.loads(request.body)

        try:
            name     = data['name']
            email    = data['email']
            password = data['password']
            contact  = data['contact']
            mbti     = data.get('mbti', '')
            gender   = data.get('gender', 'Undefined')

            email_regex    = '^[a-zA-Z0-9]([-_.]?[a-zA-Z0-9])*@[a-zA-Z0-9]([-_.]?[a-zA-Z0-9])*\.[a-zA-Z]{2,3}$'
            password_regex = '''^.*(?=.*[a-zA-Z])(?=.*\d)(?=.*[!"#$%&'()*+,\-./:;<=>?@[＼\]^_`{|}~\\)])[\w!"#$%&'()*+,\-./:;<=>?@[＼\]^`{|}~\\)]{8,45}$'''
            contact_regex  = '^\+[0-9]([ ]?[0-9]){8,49}$'
            mbti_regex     = '^[ie][ns][tf][jp]$'
            gender_list    = ['Male', 'Female', 'Undefined']

            if re.match(email_regex, email) is None:
                return JsonResponse({'message': 'INVALID_EMAIL'}, status=400)
            if re.match(password_regex, password) is None:
                return JsonResponse({'message': 'INVALID_PASSWORD'}, status=400)
            if re.match(contact_regex, contact) is None:
                return JsonResponse({'message': 'INVALID_CONTACT'}, status=400)
            if mbti != '' and not re.match(mbti_regex, mbti):
                return JsonResponse({'message': 'INVALID_MBTI'}, status=400)
            if gender not in gender_list:
                return JsonResponse({'message': 'INVALID_GENDER'}, status=400)

            user = User(
                name     = name,
                email    = email,
                password = password,
                contact  = contact,
                mbti     = mbti,
                gender   = gender,
            )

            user.full_clean()
            user.save()

        except KeyError:
            return JsonResponse({'message': 'KEY_ERROR'}, status=400)
        except ValidationError:
            return JsonResponse({'message': 'VALIDATION_ERROR'}, status=400)

        return JsonResponse({'message': 'CREATED'}, status=201)


class SigninView(View):

    def post(self, request):

        data = json.loads(request.body)

        try:
            email    = data['email']
            password = data['password']
            User.objects.get(email=email, password=password)
            return JsonResponse({'message': 'SUCCESS'}, status=200)

        except User.DoesNotExist:
            return JsonResponse({'message': 'INVALID_USER'}, status=401)
        except KeyError:
            return JsonResponse({'message': 'KEY_ERROR'}, status=400)

        return JsonResponse({'message': 'CREATED'}, status=201)
