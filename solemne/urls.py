from django.conf.urls import include, url
from . import views

urlpatterns = [

    url(r'^home/$', views.home, name = 'home'),
    url(r'^category/(?P<category_id>\d+)/$', views.category, name='category'),
    url(r'^product/(?P<product_id>\d+)/$', views.product, name='product'),
]