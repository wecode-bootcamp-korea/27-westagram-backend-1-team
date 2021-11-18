import json, re

from django.views import View
from django.http  import JsonResponse

# Create your views here.

class UsersView(View):
    def post(self, req):
        data = json.loads(req.body)
        try:
            name     = data['name']
            email    = data['email']
            password = data['password']
            contact  = data['contact']
            if 'mbti' in data:
                mbti = data['mbti']
            if 'gender' in data:
                gender = data['gender']
                if gender not in ['F', 'M', 'U']:
                    raise ValueError

        except:
            return JsonResponse({'message': 'KEY_ERROR'}, status=400)

        return JsonResponse({'RESULT': 'SUCCESS'}, status=201)
