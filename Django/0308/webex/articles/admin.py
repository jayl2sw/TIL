from django.contrib import admin
from .models import Article

# Register your models here.

# 관리자 사이트에 추가할 객체 
class ArticleAdmin(admin.ModelAdmin):
    # 어떻게 보여줄 지 정의
    list_display = ('pk', 'title', 'content', 'created_at', 'updated_at')
    list_filter = ('created_at', )
    # 무엇을 눌러서 들어갈 것인가?
    list_display_links = ('title', )
    list_per_page = 5
    ordering = ('pk',)
    
    


# 관리자 사이트 등록(Article)
admin.site.register(Article, ArticleAdmin)