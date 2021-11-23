import re

from django.core.exceptions import ValidationError

from .models import User

REGEX_EMAIL    = r'^[a-zA-Z0-9+-_.]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
REGEX_PASSWORD = r'^(?=.*[A-Za-z])(?=.*\d)(?=.*[$@$!%*#?&])[A-Za-z\d$@$!%*#?&]{8,}$'

def Validation(email,password):
    if not re.match(REGEX_EMAIL, email) :
        raise ValidationError("Email format is incorretct")
    
    if not re.match(REGEX_PASSWORD, password) :
        raise ValidationError("Password format is incorrect")

    if User.objects.filter(email=email).exists():
        raise ValidationError("Email already exists")