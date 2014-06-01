from __future__ import unicode_literals

from django.conf.urls import patterns, url

urlpatterns = patterns(
    'summary.views',
    url(r'^$', 'summary_list', name='summary_list'),
    url(r'^(?P<year>\d{4})/$', 'summary_year', name='summary_year'),
    url(r'^(?P<year>\d{4})/(?P<month>\d{1,2})/$', 'summary_month', name='summary_month'),
)
