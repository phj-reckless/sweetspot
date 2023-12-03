# sweetspot/urls.py

from django.urls import path
from . import views
from django.contrib import messages

app_name = 'sweetspot'

urlpatterns = [
    path('', views.main_view, name='main'),
    path('main/', views.main_view, name='main'),
    path('event/', views.event_view, name='event'),
    path('search/', views.list_view, name='list'),
    path('mypage/', views.mypage_view, name='mypage'),
    path('myfavorite/', views.myfavorite_view, name='myfavorite'),
]