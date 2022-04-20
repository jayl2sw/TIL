from tkinter import CASCADE
from django.db import models
from django.conf import settings
from datetime import datetime, timedelta, timezone

# Create your models here.
class Article(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=30)
    blue = models.CharField(max_length=20)
    red = models.CharField(max_length=20)
    blue_score = models.IntegerField(default=0)
    red_score = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    vws = models.IntegerField(default=0)
    
    @property
    def created_string(self):
            time = datetime.now(tz=timezone.utc) - self.created_at
            if time < timedelta(minutes=1):
                return '방금 전'
            elif time < timedelta(hours=1):
                return str(int(time.seconds / 60)) + '분 전'
            elif time < timedelta(days=1):
                return str(int(time.seconds / 3600)) + '시간 전'
            elif time < timedelta(days=7):
                time = datetime.now(tz=timezone.utc).date() - self.registered_date.date()
                return str(time.days) + '일 전'
            else:
                return False

    def __str__(self):
        return self.title

class Comment(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    color = models.BooleanField()
    content = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)


    @property
    def created_string(self):
            time = datetime.now(tz=timezone.utc) - self.created_at
            if time < timedelta(minutes=1):
                return '방금 전'
            elif time < timedelta(hours=1):
                return str(int(time.seconds / 60)) + '분 전'
            elif time < timedelta(days=1):
                return str(int(time.seconds / 3600)) + '시간 전'
            elif time < timedelta(days=7):
                time = datetime.now(tz=timezone.utc).date() - self.registered_date.date()
                return str(time.days) + '일 전'
            else:
                return False
    def __str__(self):
        return self.title