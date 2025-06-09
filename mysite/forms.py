from django.forms import ModelForm, Form
from django.forms import PasswordInput, TextInput
from django.forms import CharField
from django.contrib.auth import authenticate

from . import models


class LoginForm(Form):
    """Форма авторизации"""
    username = CharField(widget=TextInput({"autocomplete": "new-email"}))
    password = CharField(widget=PasswordInput({"autocomplete": "new-password"}))

    def clean(self):
        cleaned_data = super().clean()
        username = cleaned_data.get("username")
        password = cleaned_data.get("password")
        
        if not models.User.objects.filter(username=username).exists():
            self.add_error('username', "Пользователя с таким именем не существует")
        else:
            self.user = authenticate(username=username, password=password)
            if not self.user:
                self.add_error('password', "Неверный пароль")
            
    def get_user(self):
        return self.user
    
    
class RegisterForm(ModelForm):
    """Форма регистрации"""
    class Meta:
        model = models.User
        fields = ("username", "email", "password")
    
    def save(self):
        cleaned_data = self.cleaned_data
        user = models.User.objects.create_user(username=cleaned_data["username"], email=cleaned_data["email"], password=cleaned_data["password"])
        return user


class SolutionForm(ModelForm):
    class Meta:
        model = models.Solution
        fields = ("code", )