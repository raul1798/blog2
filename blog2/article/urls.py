from django.conf.urls import url
from django.contrib import admin

from .views import (
	post_list,
	post_create,
	post_detail,
	post_update,
	post_delete,
	users_list,
	user_article
	)

urlpatterns = [
	url(r'^$', post_list, name='list'),
	url(r'^users/$', users_list, name='users'),
	url(r'^users/(?P<pk>[0-9]+)/$', user_article, name='user_post'),
    url(r'^create/$', post_create),
    url(r'^(?P<pk>[0-9]+)/$', post_detail, name='detail'),
    url(r'^(?P<pk>[0-9]+)/edit/$', post_update, name='update'),
    url(r'^(?P<pk>[0-9]+)/delete/$', post_delete),
    #url(r'^posts/$', "<appname>.views.<function_name>"),
]