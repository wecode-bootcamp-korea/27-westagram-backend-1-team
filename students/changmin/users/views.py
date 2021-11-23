import json

from django.views           import View
from django.http            import JsonResponse
from django.db              import IntegrityError
from django.core.exceptions import ValidationError

from users.models           import User
from users.validation       import validate_check

class SignUpView(View):
    def post(self, request):

        try:
            data           = json.loads(request.body)
            user_name      = data['name']
            user_email     = data['email']
            user_password  = data['password']
            user_phone     = data['phone']
            
            user_create = User(
                name        = user_name,
                email       = user_email,
                password    = user_password,
                phone       = user_phone,
            )

            validate_check(
                user_email,
                user_password,
            )

            user_create.full_clean()
            user_create.save()
        
            return JsonResponse({'message':'SUCCESS'}, status=201)

        except IntegrityError:
            return JsonResponse({'message':'Duplicated Email exists'}, status=401)

        except KeyError:
            return JsonResponse({'message':'KEY_ERROR'}, status=400)

        except ValidationError: 
            return JsonResponse({'message':'Validation Error'}, status=400)

class SignInView(View):
    def post(self, request):

        try:
            data     = json.loads(request.body)
            user_email    = data['email']
            user_password = data['password']

            if user_email == '' or user_password == '':
                return JsonResponse({'message':'Email or Password must be entered'}, status=401)

            if not User.objects.filter(email=user_email, password=user_password).exists():
                return JsonResponse({'message':'INVALID_USER'}, status=401)

            return JsonResponse({'message':'SUCCESS'}, status=200)

        except KeyError:
            return JsonResponse({'message':'KEY_ERROR'}, status=400)