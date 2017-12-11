from django import forms


class SearchForm(forms.Form):
    region = forms.CharField(max_length=30)
    max_prise = forms.IntegerField()
    min_prise = forms.IntegerField()
    from_date = forms.DateField()
    to_date = forms.DateField()


class LoginForm(forms.Form):
    username = forms.CharField(max_length=30)
    password = forms.CharField(max_length=30)