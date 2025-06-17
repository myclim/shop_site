from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UserChangeForm
from django import forms
from user.models import UsersModel



class UserLoginForm(AuthenticationForm):
    pass 
    

class UserRegistrationForm(UserCreationForm):
    
    class Meta:
        model = UsersModel
        fields = (
            'username',
            'first_name',
            'last_name',
            'phone',
            'email',
            'password1',
            'password2',
        )


class UpdateForm(UserChangeForm):
    password = None
    class Meta:
        model = UsersModel
        fields = (
            'first_name',
            'last_name',
            'phone',
            'image',
            'email',
        )