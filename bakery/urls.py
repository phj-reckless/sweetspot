
from django.urls import path
from . import views
from django.conf import settings
from django.shortcuts import redirect

app_name = 'bakery'

urlpatterns = [
    path('', views.BakeryListView.as_view(), name='bakery_list'),
    path('<int:pk>/', views.bakery_detail_view, name='bakery_detail'),
    path('register/', views.bakery_register_view, name='bakery_register'),
    path('<int:pk>/edit/', views.bakery_edit_view, name='bakery_edit'),
    path('<int:pk>/delete/', views.bakery_delete_view, name='bakery_delete'),
]