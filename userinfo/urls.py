from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^back_index$', views.back_index),
    # url(r'^register_user$', views.register_user),
    # url(r'^login_user$', views.login_user),
    # url(r'^logout_user$', views.logout_user),
]
