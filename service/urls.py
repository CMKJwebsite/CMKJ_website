from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.view_service),
    url(r'^back_index$', views.back_index),
    url(r'^service_detail', views.view_service_detail),
]
