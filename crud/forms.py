from django import forms
from django.contrib.auth.models import User
from crud.models import UserProfileInfo

class LoginForm(forms.Form):
    username = forms.CharField(label='User Name', max_length=100, widget=forms.TextInput(attrs={'class': 'username'}))
    password = forms.CharField(label='Password',widget=forms.PasswordInput(attrs={'class': 'password:'}), max_length=100)
    

class RegisterForm(forms.Form):
    username = forms.CharField(label="User Name", max_length=50)
    password = forms.CharField(label="Password",widget=forms.PasswordInput(), max_length=50)
    email = forms.CharField(label="Email", max_length=50)
    first_name = forms.CharField(label="First Name", max_length=30)
    last_name = forms.CharField(label="Last Name", max_length=30)
    
class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    class Meta:
        model = User
        fields = ('username', 'email', 'password')
        
class UserProfileInfoForm(forms.ModelForm):
    class Meta:
        model = UserProfileInfo
        fields = {'portfolio_site', 'profile_pic'}
