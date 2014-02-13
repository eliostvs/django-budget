from django.conf.urls import patterns, url

urlpatterns = patterns(
    'category.views',
    url(r'^$', 'category_list', name='category_list'),
    url(r'^add/$', 'category_add', name='category_add'),
    url(r'^edit/(?P<slug>[\w_-]+)/$', 'category_edit', name='category_edit'),
    url(r'^delete/(?P<slug>[\w_-]+)/$', 'category_delete', name='category_delete'),
)
