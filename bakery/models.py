from django.db import models
import os
from django.conf import settings
from uuid import uuid4
from django.utils import timezone
from datetime import datetime
from config.settings.base import AUTH_USER_MODEL


class Bakery(models.Model):
    name = models.CharField(max_length=128, verbose_name='가게명')
    info = models.TextField(verbose_name='소개')
    hp = models.CharField(max_length=15, verbose_name='전화번호')
    operated_date = models.CharField(max_length=128, verbose_name='운영시간')
    address = models.CharField(max_length=128, verbose_name='주소')

    def __str__(self):
        return self.name

    class Meta:
        db_table = '빵집 리스트'
        verbose_name = '빵집 리스트'
        verbose_name_plural = '빵집 리스트'


