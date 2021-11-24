import re

from django.core.exceptions import ValidationError

REGEX_EMAIL    = r'^[a-zA-Z0-9+-_.]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
REGEX_PASSWORD = r'^(?=.*[A-Za-z])(?=.*\d)(?=.*[$@$!%*#?&])[A-Za-z\d$@$!%*#?&]{8,}$'

def validate_email(email):
    if not re.match(REGEX_EMAIL, email) :
        raise ValidationError("Email format is incorretct")
    
def validate_password(password):
    if not re.match(REGEX_PASSWORD, password) :
        raise ValidationError("Password format is incorrect")