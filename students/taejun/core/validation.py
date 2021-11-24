import re

from django.core.exceptions import ValidationError

def email_validation(email):
    EMAIL_REGEX = '^[a-zA-Z0-9]([-_.]?[a-zA-Z0-9])*@[a-zA-Z0-9]([-_.]?[a-zA-Z0-9])*\.[a-zA-Z]{2,3}$'

    if re.match(EMAIL_REGEX, email) is None:
        raise ValidationError('INVALID_EMAIL')

def password_validation(password):
    PASSWORD_REGEX = '''^.*(?=.*[a-zA-Z])(?=.*\d)(?=.*[!"#$%&'()*+,\-./:;<=>?@[＼\]^_`{|}~\\)])[\w!"#$%&'()*+,\-./:;<=>?@[＼\]^`{|}~\\)]{8,45}$'''

    if re.match(PASSWORD_REGEX, password) is None:
        raise ValidationError('INVALID_PASSWORD')

def contact_validation(contact):
    CONTACT_REGEX  = '^\+[0-9]([ ]?[0-9]){8,49}$'

    if re.match(CONTACT_REGEX, contact) is None:
        raise ValidationError('INVALID_CONTACT')

def mbti_validation(mbti):
    MBTI_REGEX     = '^[ie][ns][tf][jp]$'

    if mbti != '' and not re.match(MBTI_REGEX, mbti):
        raise ValidationError('INVALID_MBTI')

def gender_validation(gender):
    GENDER_LIST    = ['Male', 'Female', 'Undefined']

    if gender not in GENDER_LIST:
        raise ValidationError('INVALID_GENDER')
