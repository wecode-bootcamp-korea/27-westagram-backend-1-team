import json, re

from django.http  import JsonResponse
from django.views import View
from users.models import User
from django.core.exceptions import ValidationError

class SignupView(View) :
    def post(self,request) :

        data = json.loads(request.body)
    
        try: 
            name            = data['name']
            email           = data['email']
            password        = data['password']
            contact         = data['contact']
            profile         = data['profile']
                                
            regex_email     = r'^[a-zA-Z0-9+-_.]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
            regex_password  = r'^(?=.*[A-Za-z])(?=.*\d)(?=.*[$@$!%*#?&])[A-Za-z\d$@$!%*#?&]{8,}$'
            
            if User.objects.filter(email=email).exists():
                raise ValidationError("This email already used.")                    
            
            if not re.match(regex_email, email):
                return JsonResponse({"message": "Email Validation Error"}, status=400)
            
            if not re.match(regex_password, password):
                return JsonResponse({"message": "Password Validation Error"}, status=400)
            
            User.objects.create(
                name     = data['name'],
                email    = data['email'],
                password = data['password'],
                contact  = data['contact'],
                profile  = data['profile'],
                )
            
        except KeyError : 
            return JsonResponse({"message" : "KEY_ERROR"}, status=400)   
        
        return JsonResponse({"message" : "SUCCESS"}, status = 201)

        
class SignInView(View):
    def post(self, request):
        
        data = json.loads(request.body)

        try:
            email        = data['email']
            password     = data['password']

            if email == "" or password =="":
                return JsonResponse({"message": "Email or Password field is blanked."}, status=401)
            if not User.objects.filter(email=email, password=password).exists():
                return JsonResponse({"message": "INVALID_USER"}, status=401)
            return JsonResponse({"message" : "SUCCESS"}, status = 201)

        except KeyError:
            return JsonResponse({"message": "KEY_ERROR"}, status=400)