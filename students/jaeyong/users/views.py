import json, re

from django.http  import JsonResponse
from django.views import View
from users.models import User

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

            if not re.match(regex_email, email):
                return JsonResponse({"message": "Key-Error"}, status=400)
            if not re.match(regex_password, password):
                return JsonResponse({"message": "Key-Error"}, status=400)
            

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