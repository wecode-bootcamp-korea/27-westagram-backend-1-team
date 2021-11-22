import json, re

from django.views           import View
from django.http            import JsonResponse
from django.db              import IntegrityError
from django.core.exceptions import ValidationError

from users.models           import User

class SignUpView(View):
    REGEX_EMAIL    = '^[a-zA-Z0-9+-_.]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    REGEX_PASSWORD = '^(?=.*[A-Za-z])(?=.*\d)(?=.*[$@$!%*#?&])[A-Za-z\d$@$!%*#?&]{8,}$'

    def post(self, request):
        data           = json.loads(request.body)
        user_name      = data['name']
        user_email     = data['email']
        user_password  = data['password']
        user_phone     = data['phone']

        try:
            if not re.match(self.REGEX_EMAIL, user_email) or user_email == '':
                return JsonResponse({'message' : 'EMAIL_KEY_ERROR'}, status=400)

            if not re.match(self.REGEX_PASSWORD, user_password) or user_password == '':
                raise ValidationError('PASSWORD_KEY_ERROR')
            
            user_create = User(
                name        = user_name,
                email       = user_email,
                password    = user_password,
                phone       = user_phone,
            )

            user_create.full_clean()
            user_create.save()
        
            return JsonResponse({'message':'SUCCESS'}, status=201) 
        
        except IntegrityError:
            return JsonResponse({'message':'Duplicated Email exists'}, status=401)

class SignInView(View):

    def post(self, request):
        data     = json.loads(request.body)
        email    = data['email']
        password = data['password']

        try:
            if data['email'] == '' or data['password'] == '':
                return JsonResponse({'message':'KEY_ERROR'}, status=400)

            if not User.objects.filter(email=email).exists() and User.objects.filter(password=password).exists():
                return JsonResponse({'message':'INVALID_USER'}, status=401)

            return JsonResponse({'message':'SUCCESS'}, status=200)

        except ValidationError:
        	("Please enter a password of at least 8 digits")