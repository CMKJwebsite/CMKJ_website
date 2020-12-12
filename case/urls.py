from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.view_case),
    url(r'^back_index$', views.back_index),
    url(r'^case_detail', views.view_case_detail),
]
