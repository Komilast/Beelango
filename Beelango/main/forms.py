from django import forms


class RegisterForm(forms.Form):
    username = forms.CharField(max_length=20)
    email = forms.EmailField()
    password = forms.CharField(max_length=25, widget=forms.PasswordInput)
    confirm_password = forms.CharField(max_length=25, widget=forms.PasswordInput)