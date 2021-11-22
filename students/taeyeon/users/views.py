import json,re

from django.http  import JsonResponse
from django.views import View

from .models      import User

class UsersView(View) :
    def post(self,request) :
        try: 
            data           = json.loads(request.body)
            email          = data['email']
            password       = data['password']
            regex_email    = r'^[a-zA-Z0-9+-_.]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
            regex_password = r'^(?=.*[A-Za-z])(?=.*\d)(?=.*[$@$!%*#?&])[A-Za-z\d$@$!%*#?&]{8,}$'

            if re.search(regex_email,email) == None :
                return JsonResponse({"message" : "Email format is incorrect"}, status=400)

            if re.search(regex_password, password) == None :
                return JsonResponse({"message" : "Password format is incorrect"}, status=400)

            
            if User.objects.filter(email=email).exists :
                return JsonResponse({"message": "Email already exist"}, status=400)   
            

            User.objects.create(
                name     = data['name'],
                email    = data['email'],
                password = data['password'],
                phone    = data['phone'],
                mbti     = data['mbti']
                )
            
  
        except KeyError : 
            return JsonResponse({"message" : "KEY_ERROR"}, status=400)   
        
        return JsonResponse({"message" : "SUCCESS"}, status = 201)