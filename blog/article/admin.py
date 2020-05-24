from django.contrib import admin

from .models import Article

# 注册Article到admin
admin.site.register(Article)