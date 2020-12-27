from django.conf.urls import url
from . import views
app_name = 'product'
urlpatterns = [
    url(r'^back_index$', views.back_index),
    url(r'^$', views.view_product, name='product'),
    # url(r'^$', views.ProductView.as_view(), name='product'),
    url(r'^product_category', views.view_product_category, name='product_category'),
    # url(r'^product_category', views.ProductCategoryView.as_view(), name='product_category'),
    url(r'^product_name', views.view_product_detail, name='product_name'),
]
