
from django.conf import settings
from django.shortcuts import redirect
from django.contrib import messages
from .models import User
from django.http import HttpResponse


# 관리자 권한 확인
def admin_required(function):
    def wrap(request, *args, **kwargs):
        if request.user.level == '1':
            return function(request, *args, **kwargs)
        messages.info(request, "접근 권한이 없습니다.")
        return redirect('/bakery/')
    return wrap