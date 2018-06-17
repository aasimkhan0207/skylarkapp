from django.conf.urls import url
from . import views

app_name = 'fifa'

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^add_match$', views.add_match, name='add_match'),
    url(r'^getjson/', views.getjson)
]