
from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import User


class UserForm(UserCreationForm):
    user_id = forms.CharField(label="아이디")
    email = forms.EmailField(label="이메일")
    hp = forms.CharField(label="전화번호")

    class Meta:
        model = User
        fields = ["user_id", "password1", "password2", "hp", "email"]


class CustomUserChangeForm(UserChangeForm):
    password = None
    hp = forms.CharField(label='전화번호', widget=forms.TextInput(
        attrs={'class': 'form-control', 'maxlength': '11', 'oninput': "maxLengthCheck(this)",}),
    )
    email = forms.EmailField(label='이메일', widget=forms.EmailInput(
        attrs={'class': 'form-control', 'maxlength': '128',}),
    )

    class Meta:
        model = User()
        fields = ['hp', 'email']