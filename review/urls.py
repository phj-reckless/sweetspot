
from django.urls import path
from . import views
from django.conf import settings
from django.shortcuts import redirect

app_name = 'review'

urlpatterns = [
    path('', views.ReviewListView.as_view(), name='review_list'),
    path('<int:pk>/', views.review_detail_view, name='review_detail'),
    path('write/', views.review_write_view, name='review_write'),
    path('<int:pk>/edit/', views.review_edit_view, name='review_edit'),
    path('<int:pk>/delete/', views.review_delete_view, name='review_delete'),
]
