import json

from django.views           import View
from django.http            import JsonResponse
from django.core.exceptions import ValidationError

from users.models           import User
from users.validation       import validate_check

class SignUpView(View):
    def post(self, request):

        data = json.loads(request.body)

        try:
            data           = json.loads(request.body)
            user_name      = data['name']
            user_email     = data['email']
            user_password  = data['password']
            user_phone     = data['phone']
            
            user_create     = User(
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

        except KeyError:
            return JsonResponse({'message':'KEY_ERROR'}, status=400)

        except ValidationError as e: 
            return JsonResponse({'message':e.messages}, status=400)


class SignInView(View):
    def post(self, request):

        try:
            data          = json.loads(request.body)
            user_email    = data['email']

            if User.objects.filter(email=user_email).exists():
                return JsonResponse({'message':'INVALID_USER'}, status=401)
            
            return JsonResponse({'message':'SUCCESS'}, status=200)

        except KeyError:
            return JsonResponse({'message':'KEY_ERROR'}, status=400)