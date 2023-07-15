from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class SignUpForm(UserCreationForm):
    profile_img = forms.ImageField()

    class Meta:
        model = User
        fields = [
            'username',
            'email',
            'first_name',
            'last_name',
            'password1',
            'password2',
            'profile_img',
        ]
        widgets = {
            'profile_img': forms.ClearableFileInput()
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['profile_img'].widget.attrs.update({'id': 'profileimg'})


class LoginForm(forms.Form):
    username = forms.CharField(required=True, widget=forms.TextInput(
        attrs={
        'placeholder': 'Username'
        }
    ))
    password = forms.CharField(required=True, widget=forms.PasswordInput(
        attrs={
        'placeholder': 'Password'
        }
    ))