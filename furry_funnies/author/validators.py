from django.core.exceptions import ValidationError


def letters_validator(name):
    for current_char in name:
        if not current_char.isalpha():
            raise ValidationError('Your name must contain letters only!')


def passcode_validator(code):
    if len(code) != 6:
        raise ValidationError('Your passcode must be exactly 6 digits!')