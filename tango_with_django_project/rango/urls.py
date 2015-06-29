__author__ = 'lvyadong'

from django.conf.urls import patterns, url
from rango import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^about/', views.about, name='about'),
    url(r'^add_category/$', views.add_category, name='add_category'),
    url(r'^category/(?P<category_name_slug>[\w\-]+)/add_page/$', views.add_page, name='add_page'),
    # views中的category需要參數category_name_slug，就是按照下面這種方式來傳遞
    url(r'^category/(?P<category_name_slug>[\w\-]+)/$', views.category, name='category'),
)
