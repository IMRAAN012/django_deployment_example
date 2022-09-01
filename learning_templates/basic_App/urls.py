from django.conf.urls import url
from basic_App import views

#  Template Tagging
app_name = 'basic_App'

urlpatterns = [
    url(r'^relative/$',views.relative,name='relative'),
    url(r'^basic/$',views.basic,name='basic'),
    url(r'^other/$',views.other,name='other'),
]
