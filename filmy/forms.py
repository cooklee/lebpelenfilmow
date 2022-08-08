from django import forms
from django.core.exceptions import ValidationError

from filmy.models import Person


# def check_if_exist(value):
#     try:
#         Person.objects.get(first_name=value)
#         raise ValidationError("jest w bazie danych")
#     except Person.DoesNotExist:
#         pass
#
#
# def check_name(value):
#     if value == 'Gosia':
#         raise ValidationError("Tego pana nie obsługujemy")

class AddPersonForm(forms.Form):
    first_name = forms.CharField(max_length=128,
                                 widget=forms.PasswordInput(attrs={'class': 'form-input b1'}))
    last_name = forms.CharField(max_length=128)

    def clean(self):
        data = super().clean()
        if data['first_name'] == 'Sławek' and data['last_name'] == 'Bo':
            raise ValidationError("no poprostu .... NIE")
        return data
