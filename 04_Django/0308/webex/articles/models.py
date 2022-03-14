from django.db import models

# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=10)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True) # article이 생성될 때 자동으로 추가
    updated_at = models.DateTimeField(auto_now=True) # 자동으로 현재 시각을 추가
    

    def __str__(self):
        return self.title