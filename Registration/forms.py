from django import forms
from .models import Signup
from .models import Login


class SignupForm(forms.ModelForm):
    class Meta:
        model = Signup
        fields = '__all__'

class LoginForm(forms.ModelForm):
    class Meta:
        model = Login
        fields = '__all__'
