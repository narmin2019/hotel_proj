from re import search

from PIL.ImageShow import register
from django.shortcuts import render, redirect
from django.views.generic import View
from django.http import HttpResponseNotFound
from . import forms
from django.db.models import Q
from django.contrib.auth.models import User as SystemUser
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout as django_logout

from .models import *
# Create your views here.


class Home(View):
    def get(self, request):
        top_hotels = Hotel.objects.all()
        return render(request, "home.html", {'title': 'Top Hotels!', 'hotels': top_hotels})

    def post(self, request):
        form = forms.SearchForm(request.POST)
        if form.is_valid():
            form.clean()
            search_region = form.cleaned_data['region']
            if search_region:
                q = Q(region__icontains=search_region) | Q(name__icontains=search_region)
                found_hotels = Hotel.objects.filter(q)
                return render(request, "home.html", {'title': 'Search Result', 'hotels': found_hotels})


class Register(View):
    def get(self, request):
        form = UserCreationForm()
        return render(request, "register.html", {'form':form})

    def post(self, request):
        form = forms.RegisterForm(request.POST)
        if form.is_valid():
            form.clean()
            name = form.cleaned_data.get('name')
            surname = form.cleaned_data.get('surname')
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password')
            ismanager = form.cleaned_data.get('ismanager')

            if ismanager:
                pass
            else:
                user = SystemUser.objects.create_user(username=email, email=email, password=password, first_name=name,
                                                      last_name=surname)
                new_customer = Customer.objects.create(user=user)
                new_customer.save()
                authenticate(request, username=new_customer.user.username, password=new_customer.user.password)
                login(request, user)
                return redirect('home')


class Login(View):
    def get(self, request):
        return render(request, "login.html")

    def post(self, request):
        form = forms.LoginForm(request.POST)
        if form.is_valid():
            form.clean()
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password')
            user = authenticate(username=email, password=password)

            if user is not None:
                login(request, user)
                customer = Customer.objects.filter(user=user).first()
                if customer:
                    return redirect('home')
                elif user.is_staff:
                    return redirect('admin/login')
            return render(request, 'login.html', {'title': 'Invalid email or password. Try again'})
        else:
            return render(request, 'login.html', {'title': 'Please enter email and password to login'})


class HotelDetails(View):
    def get(self, request, hotel_id):
        try:
            hotel = Hotel.objects.get(pk=int(hotel_id))
        except:
            return HttpResponseNotFound()
        else:
            return render(request, "hotel.html", {'hotel': hotel})


def logout(request):
    if request.user.is_authenticated:
        django_logout(request)
        return redirect('login')


def badmethod(request):
    pass#return render('home.html', {'title':??})