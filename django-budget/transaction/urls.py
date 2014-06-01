from __future__ import unicode_literals

from django.conf.urls import patterns, url


urlpatterns = patterns(
    'transaction.views',
    url(r'^$', 'transaction_list', name='transaction_list'),
    url(r'^add/$', 'transaction_add', name='transaction_add'),
    url(r'^edit/(?P<pk>\d+)/$', 'transaction_edit', name='transaction_edit'),
    url(r'^delete/(?P<pk>\d+)/$', 'transaction_delete', name='transaction_delete'),
)
