
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.utils import timezone
from .forms import UserForm, CustomUserChangeForm
from django.utils.decorators import method_decorator
from .models import User
from django.views.generic import View
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView

def signup(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            user_id = form.cleaned_data.get('user_id')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(user_id=user_id, password=raw_password)
            login(request, user)
            return redirect('users:login')
    else:
        form = UserForm()
    return render(request, 'users/signup.html', {'form': form})

@login_required
def profile_view(request):
    if request.method == 'GET':
        return render(request, 'users/profile.html')

@login_required
def profile_update_view(request):
    user = request.user
    if request.method == 'POST':

        email = request.POST['email']
        hp = request.POST['hp']

        user.email = email
        user.hp = hp
        user.save()

        return redirect('users/profile')

    else:
        return render(request, 'users/profile_update.html', context={'user': user,})
        """
        user_change_form = CustomUserChangeForm(request.POST, instance=request.user)

        if user_change_form.is_valid():
            user_change_form.save()
            messages.success(request, '회원정보가 수정되었습니다.')
            return render(request, 'users/profile.html')
        else:
            user_change_form = CustomUserChangeForm(instance=request.user)

            return render(request, 'users/profile_update.html', {'user_change_form': user_change_form})
        """
