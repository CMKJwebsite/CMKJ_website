from django.conf.urls import url
from . import views
app_name = 'service'
urlpatterns = [
    # url(r'^$', views.view_service),
    url(r'^$', views.ServiceView.as_view(), name='Service'),
    url(r'^back_index$', views.back_index),
    url(r'^service_detail', views.view_service_detail),
]
