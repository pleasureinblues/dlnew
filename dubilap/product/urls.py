from django.conf.urls import patterns, url
from product import views

urlpatterns = patterns('',
       url(r'^$', views.index, name='index'),
       url(r'^product_page/(?P<product_id>\d+)/$', views.product_page, name='prdocut_page'),
       url(r'^categories/$', views.categories, name='categories'),
       url(r'^category/(?P<cat_name_slug>[-\w]+)/$', views.category_page, name='category'),
       url(r'^brands/$', views.brands, name='brands'),
       url(r'^brand/(?P<brand_name_slug>[-\w]+)/$', views.brand_page, name='brand_page'),
       url(r'^price/(?P<price_pattern>[-\w]+)/$', views.price, name='price'),
       url(r'^customer_contact/$', views.ps_contact, name='price'),

       )
