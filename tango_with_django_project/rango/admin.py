from django.contrib import admin
from rango.models import Category, Page

# 修改admin的pages頁面，詳見官方入門教程第二章
class PageAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'url')

# Register your models here.
# This will register the models with the admin interface.
admin.site.register(Category)
admin.site.register(Page, PageAdmin)
