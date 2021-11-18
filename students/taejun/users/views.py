import json, re

from django.views import View
from django.http  import JsonResponse

from users.models import User

class SignupView(View):
    def post(self, req):
        data = json.loads(req.body)
        try:
            name     = data['name']
            email    = data['email']
            password = data['password']
            contact  = data['contact']

            email_regex = '^[a-zA-Z0-9]([-_.]?[a-zA-Z0-9])*@[a-zA-Z0-9]([-_.]?[a-zA-Z0-9])*\.[a-zA-Z]{2,3}$'
            password_regex = '''^.*(?=.*[a-zA-Z])(?=.*\d)(?=.*[!"#$%&'()*+,\-./:;<=>?@[＼\]^_`{|}~\\)])[\w!"#$%&'()*+,\-./:;<=>?@[＼\]^`{|}~\\)]{8,45}$'''
            contact_regex = '^\d{11}$'

            if re.match(email_regex, email) is None or re.match(password_regex, password) is None or re.match(contact_regex, contact) is None:
                raise ValueError

            user          = User()
            user.name     = name
            user.email    = email
            user.password = password
            user.contact  = contact

            if 'mbti' in data:
                mbti = data['mbti']
                if re.match('[ie][ns][tf][jp]', mbti):
                    user.mbti = mbti
                else:
                    raise ValueError

            if 'gender' in data:
                gender = data['gender']
                if gender in ['F', 'M', 'U']:
                    user.gender = gender
                else:
                    raise ValueError

            user.full_clean()
            user.save()

        except:
            return JsonResponse({'message': 'KEY_ERROR'}, status=400)

        return JsonResponse(
            {'message': 'success - created user('+str(user.id)+')'},
            status=201
        )
