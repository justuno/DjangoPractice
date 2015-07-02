from django.contrib import admin
from rango.models import Category, Page, UserLike
from rango.models import UserProfile

# 修改admin的pages頁面，詳見官方入門教程第二章
class PageAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'url')

# Add in this class to customized the Admin Interface
# 後臺添加一個新的category時，填寫名字的時候，slug會自動填寫相同的字符
class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name', )}

# Register your models here.
# This will register the models with the admin interface.
# Update the registeration to include this customised interface
admin.site.register(Category, CategoryAdmin)
admin.site.register(Page, PageAdmin)
admin.site.register(UserProfile)
admin.site.register(UserLike)
