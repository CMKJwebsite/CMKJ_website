from django.contrib import admin
from .models import ProductCategory, Product

# Register your models here.


class ProductCategoryManager(admin.ModelAdmin):
    # 设置列表可显示的字段
    list_display = ['id', 'c_category_name', 'c_category_alias', 'c_parent_catalog', 'c_category_description',
                    'c_SEO_title', 'c_SEO_Keyword', 'c_category_thumbnail', 'c_PC_advertisement',
                    'c_Mobile_advertisement']
    list_display_links = ['id', 'c_category_name']
    list_filter = ['id', 'c_category_name']
    search_fields = ['id', 'c_category_name']


admin.site.register(ProductCategory, ProductCategoryManager)


class ProductManager(admin.ModelAdmin):
    # 设置列表可显示的字段
    list_display = ['id', 'p_name', 'p_price', 'p_details', 'p_picture']
    list_display_links = ['id', 'p_name']
    list_filter = ['id', 'p_name']
    search_fields = ['id', 'p_name']


admin.site.register(Product, ProductManager)
