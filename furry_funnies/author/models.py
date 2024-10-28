from django.core.validators import MinLengthValidator, MaxLengthValidator
from django.db import models

from furry_funnies.author.validators import letters_validator, passcode_validator


class Author(models.Model):
    first_name = models.CharField(
        max_length=40,
        validators=[
            MinLengthValidator(4),
            letters_validator],
        verbose_name = 'First Name:',
    )

    last_name = models.CharField(
        max_length=50,
        validators=[
            MinLengthValidator(2),
            letters_validator,
        ],
        verbose_name='Last Name:',
    )

    passcode = models.CharField(
        validators=[
            MinLengthValidator(6, 'Your passcode must be exactly 6 digits!'),
            MaxLengthValidator(6, 'Your passcode must be exactly 6 digits!'),
            passcode_validator,
        ],
        help_text='Your passcode must be a combination of 6 digits',
        verbose_name='Passcode:'
    )

    pets_number = models.PositiveSmallIntegerField(
        verbose_name='Pets Number:'
    )

    info = models.TextField(
        null=True,
        blank=True,
    )

    image_url = models.URLField(
        null=True,
        blank=True,
        verbose_name='"Profile Image URL:'
    )


    @property
    def full_name(self):
        if self.first_name and self.last_name:
            return f'{self.first_name} {self.last_name}'
        if self.first_name:
            return f'{self.first_name}'
        if self.last_name:
            return f'{self.last_name}'
        return None
