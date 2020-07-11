from django import forms
from django.core.exceptions import ValidationError
import re


from .models import AddCourse, MainAdminRegister


class AddCourseForm(forms.ModelForm):
    class Meta:
        model = AddCourse
        fields = '__all__'

    def clean_fee(self):
        fee = self.cleaned_data['fee']
        if fee >= 3000:
            return fee
        else:
            raise ValidationError('Fee must be greater than 3000..')

    def clean_name(self):
        name1 = self.cleaned_data['name'].title()
        name = re.findall(r'^[A-Za-z]*$', name1)
        return name


class MainAdminRegisterForm(forms.ModelForm):
    password = forms.CharField(max_length=60, widget=forms.PasswordInput)
    class Meta:
        model = MainAdminRegister
        fields = '__all__'

    def clean_username(self):
        username = self.cleaned_data['username'].title()
        if len(username)>=3:
            return username
        else:
            raise ValidationError('Username must be more than 2 alphabets' )

    def clean_password(self):
        password= self.cleaned_data['password']
        if len(password)>=8:
            return password
        else:
            raise ValidationError('password must be more than 8 characters')


class AdminLoginForm(forms.Form):
    username = forms.CharField(min_length=4)
    password = forms.CharField(min_length=8, widget=forms.PasswordInput)

