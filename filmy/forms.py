from django import forms
from django.core.exceptions import ValidationError

from filmy.models import Person, Film, Comment


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

class AddPersonForm(forms.ModelForm):

    class Meta:
        model = Person
        fields = '__all__'

class AddMovieForm(forms.ModelForm):

    class Meta:
        model = Film
        fields = '__all__'


class AddCommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ['text']




