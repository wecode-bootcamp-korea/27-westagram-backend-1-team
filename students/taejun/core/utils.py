import re, json, requests

import jwt
from django.core.exceptions import ValidationError
from django.http            import JsonResponse

from users.models           import User
from my_settings            import SECRET_KEY, ALGORITHM

class Validation:
    def email_validation(email):
        EMAIL_REGEX = '^[a-zA-Z0-9]([-_.]?[a-zA-Z0-9])*@[a-zA-Z0-9]([-_.]?[a-zA-Z0-9])*\.[a-zA-Z]{2,3}$'

        if re.match(EMAIL_REGEX, email) is None:
            raise ValidationError('INVALID_EMAIL')

    def password_validation(password):
        PASSWORD_REGEX = '''^.*(?=.*[a-zA-Z])(?=.*\d)(?=.*[!"#$%&'()*+,\-./:;<=>?@[＼\]^_`{|}~\\)])[\w!"#$%&'()*+,\-./:;<=>?@[＼\]^`{|}~\\)]{8,45}$'''

        if re.match(PASSWORD_REGEX, password) is None:
            raise ValidationError('INVALID_PASSWORD')

    def contact_validation(contact):
        CONTACT_REGEX = '^\+[0-9]([ ]?[0-9]){8,49}$'

        if re.match(CONTACT_REGEX, contact) is None:
            raise ValidationError('INVALID_CONTACT')

    def mbti_validation(mbti):
        MBTI_REGEX = '^[ie][ns][tf][jp]$'

        if mbti != '' and not re.match(MBTI_REGEX, mbti):
            raise ValidationError('INVALID_MBTI')

    def gender_validation(gender):
        GENDER_LIST = ['Male', 'Female', 'Undefined']

        if gender not in GENDER_LIST:
            raise ValidationError('INVALID_GENDER')

    def image_validation(image):
        IMAGE_TYPE = [
            'image/gif',
            'image/png',
            'image/jpeg',
            'image/svg+xml'
        ]

        if len(image) > 150:
            raise requests.RequestException

        image = requests.get(image)

        if image.status_code != 200:
            raise requests.RequestException

        if image.headers['content-type'] not in IMAGE_TYPE:
            raise requests.RequestException



def authorization(func):
    def wrapper(self, request, *args, **kwargs):
        try:
            jwt_token = request.headers.get('Authorization')

            if not jwt_token:
                return JsonResponse({'message': 'TOKEN_ERROR'}, status=400)

            payload        = jwt.decode(
                jwt_token,
                SECRET_KEY,
                algorithms=[ALGORITHM]
            )
            user           = User.objects.get(id=payload['user-id'])
            request.user   = user

            return func(self, request, *args, **kwargs)

        except jwt.exceptions.DecodeError:
            return JsonResponse({'message': 'INVALID_TOKEN'}, status=400)

        except User.DoesNotExist:
            return JsonResponse({'message': 'INVALID_USER'}, status=400)

    return wrapper
