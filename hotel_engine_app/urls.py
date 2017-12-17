from django.conf.urls import url, include
from . import views

urlpatterns = [
    url(r'^(?:search)?$', views.Home.as_view(), name='home'),
    url(r'^register$', views.Register.as_view(), name='register'),
    url(r'^login$', views.Login.as_view(), name='login'),
    url(r'^hotel/(?P<hotel_id>\d+)$', views.HotelDetails.as_view(), name='hotel')
]