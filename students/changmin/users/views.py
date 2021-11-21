import json, re

from django.views     import View
from django.http      import JsonResponse
from users.models     import User

class UserView(View):
     def post(self, request):
        data           = json.loads(request.body)
        regex_email    = '[a-zA-Z0-9]+\.?\w*@\w+[.]?\w*[.]+\w{2,3}'
        regex_password = '(?=.*[A-Za-z])(?=.*\d)(?=.*[~!@#$^&*()+|=])[A-Za-z\d~!@#$%^&*()+|=]{8,}'

        try:
            if data['email'] == '' or data['password'] == '':
                raise ValueError
            elif re.match(regex_email, data['email']) is None or re.match(regex_password, data['password']) is None:
                return JsonResponse({'message':'Email or Password is not correct'}, status = 400)
            user_create = User.objects.create(
                name        = data['name'],
                email       = data['email'],
                password    = data['password'],
                phone       = data['phone']
            )
            User.full_clean(user_create)
            User.save(user_create)
            return JsonResponse({'message':'SUCESS'},status=201)
        except ValueError:
            return JsonResponse({'message' : 'KEY_ERROR'}, status=400)