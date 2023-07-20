# custom validation fields for our pokemon models

from django.core.exceptions import ValidationError

import re

# create Function validator for my Pokemon names

def validate_name(name):
    namePattern = r'^[A-Z][a-z]*$' #only letters, starts with capital

    doesNameMatchPattern = re.match(namePattern, name) # is the name formatted in accordance with namePattern

    if doesNameMatchPattern:
        return name
    else:
        raise ValidationError("Improper name format", params={'name' : name})