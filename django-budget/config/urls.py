from django.conf.urls import include, patterns, url
from django.conf.urls.i18n import i18n_patterns
from django.contrib import admin

admin.autodiscover()


urlpatterns = patterns(
    '',
    url(r'^$',
        'base.views.index',
        name='index'),

    url(r'^i18n/',
        include('django.conf.urls.i18n')),
)

urlpatterns += i18n_patterns(
    '',

    url(r'^login/$',
        'django.contrib.auth.views.login',
        name='login'),

    url(r'^logout/$',
        'django.contrib.auth.views.logout_then_login',
        name='logout'),

    url(r'^dashboard/$',
        'dashboard.views.dashboard',
        name='dashboard'),

    url(r'^setup/$',
        'base.views.setup',
        name='setup'),

    url(r'^budget/',
        include('budget.urls', namespace='budget')),

    url(r'^category/',
        include('category.urls', namespace='category')),

    url(r'^admin/',
        include(admin.site.urls)),

    url(r'^transaction/',
        include('transaction.urls', namespace='transaction')),

    url(r'^summary/',
        include('summary.urls', namespace='summary')),
)
