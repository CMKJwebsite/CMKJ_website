from django.conf.urls import url
from . import views
app_name = 'new_center'
urlpatterns = [
    url(r'^$', views.new_center)
]
