
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.utils import timezone
from django.utils.decorators import method_decorator
from django.views.generic import View
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView


def main_view(request):
    return render(request, 'sweetspot/main.html')


def event_view(request):
    return render(request, 'sweetspot/event.html')


def list_view(request):
    return render(request, 'bakery/bakery_list.html')

@login_required
def mypage_view(request):
    return render(request, 'sweetspot/mypage.html')

@login_required
def myfavorite_view(request):
    return render(request, 'sweetspot/myfavorite.html')
