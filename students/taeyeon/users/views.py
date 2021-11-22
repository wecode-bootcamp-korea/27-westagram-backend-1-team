import json,re

from django.http            import JsonResponse
from django.views           import View
from django.core.exceptions import ValidationError

from .models                import User

class UsersView(View) :
    def post(self,request) :
        try: 
            data           = json.loads(request.body)
            email          = data['email']
            password       = data['password']
            regex_email    = r'^[a-zA-Z0-9+-_.]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
            regex_password = r'^(?=.*[A-Za-z])(?=.*\d)(?=.*[$@$!%*#?&])[A-Za-z\d$@$!%*#?&]{8,}$'

            if re.match(regex_email, email) == None :
                raise ValidationError("Email format is incorrect")
            if re.match(regex_password, password) == None :
                raise ValidationError("Password format is incorrect")
            if User.objects.filter(email=email).exists():
                raise ValidationError("Email already exists")

            User.objects.create(
                name     = data['name'],
                email    = data['email'],
                password = data['password'],
                phone    = data['phone'],
                mbti     = data.get('mbti', '')
                )        
        
        except ValidationError as e : 
            return JsonResponse({"message" : e.message }, status=400)
        except KeyError :
            return JsonResponse({"message" : "KEY_ERROR"}, status=400)

        return JsonResponse({"message" : "SUCCESS"}, status = 201)