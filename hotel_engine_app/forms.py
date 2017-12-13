from django import forms


class SearchForm(forms.Form):
    region = forms.CharField(max_length=30, required=False)
    max_prise = forms.IntegerField(required=False)
    min_prise = forms.IntegerField(required=False)
    #from_date = forms.DateField(required=False, input_formats=['%d/%m/%y'])
    #to_date = forms.DateField(required=False, input_formats=['%d/%m/%y'])


class LoginForm(forms.Form):
    username = forms.CharField(max_length=30)
    password = forms.CharField(max_length=30)