import re

def validation(email, password, contact, mbti, gender):
    email_regex    = '^[a-zA-Z0-9]([-_.]?[a-zA-Z0-9])*@[a-zA-Z0-9]([-_.]?[a-zA-Z0-9])*\.[a-zA-Z]{2,3}$'
    password_regex = '''^.*(?=.*[a-zA-Z])(?=.*\d)(?=.*[!"#$%&'()*+,\-./:;<=>?@[＼\]^_`{|}~\\)])[\w!"#$%&'()*+,\-./:;<=>?@[＼\]^`{|}~\\)]{8,45}$'''
    contact_regex  = '^\+[0-9]([ ]?[0-9]){8,49}$'
    mbti_regex     = '^[ie][ns][tf][jp]$'
    gender_list    = ['Male', 'Female', 'Undefined']

    if re.match(email_regex, email) is None:
        return 'INVALID_EMAIL'
    if re.match(password_regex, password) is None:
        return 'INVALID_PASSWORD'
    if re.match(contact_regex, contact) is None:
        return 'INVALID_CONTACT'
    if mbti != '' and not re.match(mbti_regex, mbti):
        return 'INVALID_MBTI'
    if gender not in gender_list:
        return 'INVALID_GENDER'

    return None
