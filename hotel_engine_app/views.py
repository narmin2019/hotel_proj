from django.shortcuts import render
from django.views.generic import View
from .models import Hotel as HotelModel
from django.http import HttpResponseNotFound
# Create your views here.


class Home(View):
    def get(self, request):
        return render(request, "home.html", {'title': 'Top Hotels from view!'})


class Register(View):
    def get(self, request):
        return render(request, "register.html")



class Login(View):
    def get(self, request):
        return render(request, "login.html")


class Hotel(View):
    def get(self, request, hotel_id):
        try:
            hotel = HotelModel.objects.get(pk=int(hotel_id))
        except:
            return HttpResponseNotFound()
        else:
            return render(request, "hotel.html", {'hotel': hotel})