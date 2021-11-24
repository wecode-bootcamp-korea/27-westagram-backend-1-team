import json

import bcrypt

from django.views           import View
from django.http            import JsonResponse
from django.core.exceptions import ValidationError

from users.models    import User
from core.validation import (
    email_validation,
    contact_validation,
    password_validation,
    mbti_validation,
    gender_validation
)

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

            email_validation(email)
            contact_validation(contact)
            password_validation(password)
            mbti_validation(mbti)
            gender_validation(gender)

            hashed_password = bcrypt.hashpw(
                password.encode('utf-8'),
                bcrypt.gensalt()
            ).decode('utf-8')

            user = User(
                name     = name,
                email    = email,
                password = hashed_password,
                contact  = contact,
                mbti     = mbti,
                gender   = gender,
            )

            user.full_clean()
            user.save()

        except KeyError:
            return JsonResponse({'message': 'KEY_ERROR'}, status=400)

        except ValidationError as e:
            return JsonResponse({'message': e.messages}, status=400)

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
