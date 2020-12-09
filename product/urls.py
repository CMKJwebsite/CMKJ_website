from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^back_index$', views.back_index),
    url(r'^$', views.view_product, name='product'),
    url(r'^product_category', views.view_product_category),
    url(r'^product_name', views.view_product_detail),
]
