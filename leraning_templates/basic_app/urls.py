from django.conf.urls import url
from django.urls.resolvers import URLPattern
from basic_app import views

app_name = 'basic_app'

urlpatterns = [
    url(r'^relative/$',views.relative,name='relative'),
    url(r'^other/$',views.other,name='other'),
]