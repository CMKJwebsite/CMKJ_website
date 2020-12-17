from django.contrib import admin
from .models import UserInfo

# Register your models here.


class UserInfoManager(admin.ModelAdmin):
    """
    注册model
    """
    # 设置列表可显示的字段
    list_display = ['id', 'u_user', 'u_telephone']
    list_display_links = ['id', 'u_user']
    list_filter = ['id', 'u_user']
    search_fields = ['id', 'u_user']


admin.site.register(UserInfo, UserInfoManager)
