from django import forms

from furry_funnies.author.models import Author


class BaseAuthorForm(forms.ModelForm):
    # passcode = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = Author
        fields = ['first_name', 'last_name', 'passcode', 'pets_number']
        # widgets = {
        #     'passcode': PasswordInput(attrs={'placeholder': 'Enter 6 digits...'})
        #
        # }


class CreateAuthorForm(BaseAuthorForm):
    pass


class EditAuthorForm(forms.ModelForm):
    class Meta:
        model = Author
        exclude = ('passcode',)