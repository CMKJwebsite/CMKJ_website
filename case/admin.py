from django.contrib import admin
from .models import Case

# Register your models here.


class CaseManager(admin.ModelAdmin):
    """
    注册model
    """
    # 设置列表可显示的字段
    list_display = ['id', 'c_name', 'c_category', 'c_introduction', 'c_background', 'c_challenge', 'c_details',
                    'c_highlights', 'c_reviews', 'c_picture']
    list_display_links = ['id', 'c_name']
    list_filter = ['id', 'c_name']
    search_fields = ['id', 'c_name']


admin.site.register(Case, CaseManager)
admin.site.site_header = '陕西慈铭科技有限公司官网后台管理'  # 设置header
admin.site.site_title = '陕西慈铭科技有限公司'  # 设置title
