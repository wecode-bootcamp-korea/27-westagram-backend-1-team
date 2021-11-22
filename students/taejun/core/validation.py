import re

from django.core.exceptions import ValidationError

def validation(email, password, contact, mbti, gender):
    email_regex    = '^[a-zA-Z0-9]([-_.]?[a-zA-Z0-9])*@[a-zA-Z0-9]([-_.]?[a-zA-Z0-9])*\.[a-zA-Z]{2,3}$'
    password_regex = '''^.*(?=.*[a-zA-Z])(?=.*\d)(?=.*[!"#$%&'()*+,\-./:;<=>?@[＼\]^_`{|}~\\)])[\w!"#$%&'()*+,\-./:;<=>?@[＼\]^`{|}~\\)]{8,45}$'''
    contact_regex  = '^\+[0-9]([ ]?[0-9]){8,49}$'
    mbti_regex     = '^[ie][ns][tf][jp]$'
    gender_list    = ['Male', 'Female', 'Undefined']

    if re.match(email_regex, email) is None:
        raise ValidationError('INVALID_EMAIL')
    if re.match(password_regex, password) is None:
        raise ValidationError('INVALID_PASSWORD')
    if re.match(contact_regex, contact) is None:
        raise ValidationError('INVALID_CONTACT')
    if mbti != '' and not re.match(mbti_regex, mbti):
        raise ValidationError('INVALID_MBTI')
    if gender not in gender_list:
        raise ValidationError('INVALID_GENDER')
