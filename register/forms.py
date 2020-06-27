from django import forms
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

# Creating customer user creation form for registration

class RegisterForm(UserCreationForm):
    first_name = forms.CharField()
    last_name = forms.CharField()
    email = forms.EmailField()

    class Meta():
        # This tells django what model to base the form off of and what order to
        # assign the fields.
        model = User
        fields = ['username', 'first_name', 'last_name','email' ,'password1',
                  'password2']
