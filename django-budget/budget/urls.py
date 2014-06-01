from __future__ import unicode_literals

from django.conf.urls import patterns, url

urlpatterns = patterns(
    'budget.views',
    # Budget
    url(r'^$', 'budget_list', name='budget_list'),
    url(r'^add/$', 'budget_add', name='budget_add'),
    url(r'^edit/(?P<slug>[\w-]+)/$', 'budget_edit', name='budget_edit'),
    url(r'^delete/(?P<slug>[\w-]+)/$', 'budget_delete', name='budget_delete'),
    # Estimate
    url(r'^(?P<slug>[\w-]+)/estimate/$', 'estimate_list', name='estimate_list'),
    url(r'^(?P<slug>[\w-]+)/estimate/add/$', 'estimate_add', name='estimate_add'),
    url(r'^(?P<slug>[\w-]+)/estimate/edit/(?P<pk>\d+)/$', 'estimate_edit', name='estimate_edit'),
    url(r'^(?P<slug>[\w-]+)/estimate/delete/(?P<pk>\d+)/$', 'estimate_delete', name='estimate_delete'),
)
