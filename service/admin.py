from django.contrib import admin
from .models import Service

# Register your models here.


class ServiceManager(admin.ModelAdmin):
    # 设置列表可显示的字段
    list_display = ['id', 's_name', 's_category', 's_introduction', 's_details']
    list_display_links = ['id', 's_name']
    list_filter = ['id', 's_name']
    search_fields = ['id', 's_name']


admin.site.register(Service, ServiceManager)
