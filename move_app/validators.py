# custom validation fields for our moves models

from django.core.exceptions import ValidationError

import re

# create Function validator for my moves names

def validate_move_name(name):
    namePattern = r'^[a-zA-Z]+ ?[a-zA-Z]+$' #only letters, starts with capital

    doesNameMatchPattern = re.match(namePattern, name) # is the name formatted in accordance with namePattern

    if doesNameMatchPattern:
        return name
    else:
        raise ValidationError("Improper Format")