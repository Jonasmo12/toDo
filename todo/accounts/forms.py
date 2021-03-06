from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError


class CreateUserForm(UserCreationForm):

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

    def clean(self):
        email = self.cleaned_data.get('email')
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password1')

        if User.objects.filter(email=email).exists():
            raise ValidationError("Email exists")

        if User.objects.filter(username=username).exists():
            raise ValidationError('Username in use')

        if username == password:
            raise ValidationError('Username can not be used as password')
        return self.cleaned_data
