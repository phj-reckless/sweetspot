from django.db import models
import os
from django.conf import settings
from django.db import models
from uuid import uuid4
from django.utils import timezone
from datetime import datetime
from config.settings import AUTH_USER_MODEL


class Review(models.Model):
    writer = models.ForeignKey(AUTH_USER_MODEL, on_delete=models.CASCADE, null=True, verbose_name='작성자')
    title = models.CharField(max_length=128, verbose_name='제목')
    content = models.TextField(verbose_name='내용')
    registered_date = models.DateTimeField(auto_now_add=True, verbose_name='등록시간')
    order = models.IntegerField(default=1)

    def __str__(self):
        return self.title

    class Meta:
        db_table = '리뷰'
        verbose_name = '리뷰'
        verbose_name_plural = '리뷰'

