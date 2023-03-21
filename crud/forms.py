from django import forms


class LoginForm(forms.Form):
    username = forms.CharField(label='User Name', max_length=100)
    password = forms.CharField(label='Password',widget=forms.PasswordInput(), max_length=100)
    

class RegisterForm(forms.Form):
    username = forms.CharField(label="User Name", max_length=50)
    password = forms.CharField(label="Password",widget=forms.PasswordInput(), max_length=50)
    email = forms.CharField(label="Email", max_length=50)
    first_name = forms.CharField(label="First Name", max_length=30)
    last_name = forms.CharField(label="Last Name", max_length=30)
