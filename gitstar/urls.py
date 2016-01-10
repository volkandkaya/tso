from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.gitstar_list, name='gitstar_list'),
]
