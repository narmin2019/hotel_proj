from re import search

from PIL.ImageShow import register
from django.shortcuts import render
from django.views.generic import View
from .models import Hotel
from django.http import HttpResponseNotFound
from . import forms
from django.db.models import Q
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
        return render(request, "register.html")


class Login(View):
    def get(self, request):
        return render(request, "login.html")


class HotelDetails(View):
    def get(self, request, hotel_id):
        try:
            hotel = Hotel.objects.get(pk=int(hotel_id))
        except:
            return HttpResponseNotFound()
        else:
            return render(request, "hotel.html", {'hotel': hotel})