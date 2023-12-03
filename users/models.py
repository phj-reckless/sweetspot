from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
import os
from django.conf import settings
from django.utils import timezone
from datetime import datetime
from uuid import uuid4
from .choice import *


class UserManager(BaseUserManager):
    def create_user(self, user_id, password, email, hp, auth, **extra_fields):
        user = self.model(
            user_id = user_id,
            email = email,
            hp = hp,
            auth = auth,
            **extra_fields
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, user_id, password, email=None, hp=None, auth=None):
        user = self.create_user(user_id, password, email, hp, auth)
        user.is_superuser = True
        user.is_staff = True
        user.is_admin = True
        user.level = 1
        user.save(using=self._db)
        return user


class User(AbstractBaseUser, PermissionsMixin):

    objects = UserManager()

    user_id = models.CharField(max_length=20, verbose_name="아이디", unique=True)
    password = models.CharField(max_length=256, verbose_name="비밀번호")
    email = models.EmailField(max_length=128, verbose_name="이메일", null=True, unique=True)
    hp = models.CharField(max_length=11, verbose_name="전화번호", null=True, unique=True)
    level = models.CharField(choices=LEVEL_CHOICES, max_length=18, verbose_name="등급", default=2)
    auth = models.CharField(max_length=10, verbose_name="인증번호", null=True)

    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    USERNAME_FIELD = 'user_id'
    REQUIRED_FIELDS = ['email']

    def __str__(self):
        return self.user_id

    class Meta:
        db_table = "회원목록"
        verbose_name = "사용자"
        verbose_name_plural = "사용자"
