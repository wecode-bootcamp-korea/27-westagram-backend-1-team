import json, re

from django.views           import View
from django.http            import JsonResponse
from django.core.exceptions import ValidationError

from users.models    import User
from core.validation import validation

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

            validation(
                email,
                password,
                contact,
                mbti,
                gender
            )

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

        except ValidationError as e:
            if 'message' in e.__dict__:
                return JsonResponse({'message': e.message}, status=400)

            e = e.error_dict

            if 'email' in e:
                msg = 'INVALID_EMAIL'
            elif 'name' in e:
                msg = 'INVALID_NAME'
            elif 'password' in e:
                msg = 'INVALID_PASSWORD'
            elif 'contact' in e:
                msg = 'INVALID_CONTACT'
            elif 'mbti' in e:
                msg = 'INVALID_MBTI'
            elif 'gender' in e:
                msg = 'INVALID_GENDER'
            else:
                msg = 'VALIDATION_ERROR'

            return JsonResponse({'message': msg}, status=400)

        return JsonResponse({'message': 'CREATED'}, status=201)


class SigninView(View):
    def post(self, request):
        data = json.loads(request.body)

        try:
            email    = data['email']
            password = data['password']

            if not User.objects.filter(email=email, password=password).exists():
                return JsonResponse({'message': 'INVALID_USER'}, status=401)

            return JsonResponse({'message': 'SUCCESS'}, status=200)

        except KeyError:
            return JsonResponse({'message': 'KEY_ERROR'}, status=400)
