from django.shortcuts import render
from django.views.generic import View
from django.http import HttpResponse
# Create your views here.


class Home(View):
    def get(self, request):
        if request.method == 'GET':
            return render(request, "home.html")


class Register(View):
    pass


class Login(View):
    pass


class Hotel(View):
    pass
