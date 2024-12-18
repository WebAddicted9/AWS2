from django import forms
from .models import myuser
from django.contrib.auth.forms import UserCreationForm , AuthenticationForm


# class FormDataForm(forms.ModelForm):
#     class Meta:
#         model = FormData
#         fields = ['name', 'mobile_no']


class Custom_Form(UserCreationForm):

    password1 = forms.CharField(label='Password' ,widget=forms.TextInput(attrs={'class':'form-control'}))
    password2 = forms.CharField(label='Password Confirmation' ,widget=forms.TextInput(attrs={'class':'form-control'}))

    class Meta:

        model = myuser
        fields = ['username','email','mobile_no']
        widgets = {

            'username':forms.TextInput(attrs={'class':'form-control'}),
            'email':forms.EmailInput(attrs={'class':'form-control'}),
            'mobile_no':forms.TextInput(attrs={'class':'form-control'}),
        
        }

class Login_form(AuthenticationForm):

    username = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control'}))