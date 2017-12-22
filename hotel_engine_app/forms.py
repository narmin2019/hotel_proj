from django import forms


class SearchForm(forms.Form):
    region = forms.CharField(max_length=30, required=False)
    max_prise = forms.IntegerField(required=False)
    min_prise = forms.IntegerField(required=False)


class LoginForm(forms.Form):
    email = forms.CharField(max_length=30, required=True)
    password = forms.CharField(max_length=30, required=True)


class RegisterForm(forms.Form):
    name = forms.CharField(max_length=30, required=True)
    surname = forms.CharField(max_length=30, required=True)
    email = forms.EmailField(required=True)
    password = forms.PasswordInput()
    ismanager = forms.CheckboxInput()