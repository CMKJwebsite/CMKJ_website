from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.about),
    url(r'^back_index$', views.back_index),
]