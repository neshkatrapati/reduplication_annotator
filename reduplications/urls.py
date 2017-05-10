from django.conf.urls import url

from . import views

urlpatterns = [
	url(r'^s/', views.search, name='search'),
	url(r'^r/(?P<redup_id>\d+)/', views.single_redup, name='single_redup'),
    url(r'^(?P<page_id>\d+)/', views.index, name='index'),

]