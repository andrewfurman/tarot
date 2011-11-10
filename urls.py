from django.conf.urls.defaults import *
from django.conf.urls.defaults import patterns, include, url
from django.conf import settings

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    (r'^predictions/$', 'predictions.views.index'),
    (r'^predictions/(?P<prediction_id>\d+)/$', 'predictions.views.detail'),
    (r'^predictions/(?P<prediction_id>\d+)/results/$', 'predictions.views.results'),
    (r'^predictions/(?P<prediction_id>\d+)/vote/$', 'predictions.views.vote'),
    (r'^predictions/new/$', 'predictions.views.newprediction'),
    (r'^users/$', 'predictions.views.userlist'),
    (r'^users/(?P<user_id>\d+)/$', 'predictions.views.userprofile'),
    (r'^accounts/login/$', 'django.contrib.auth.views.login'),
    (r'^accounts/logout/$', 'django.contrib.auth.views.logout'),
    (r'^accounts/profile/$', 'predictions.views.index'),
	
    # Examples:
    # url(r'^$', 'oursite.views.home', name='home'),
    # url(r'^oursite/', include('oursite.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)


if settings.DEBUG:
    urlpatterns += patterns('',
        (r'^predictions/site_media/(?P<path>.*)$', 'django.views.static.serve',
		        {'document_root': '/Users/furmanx/Desktop/oursite/predictions/static', 'show_indexes': True}),
		(r'^users/site_media/(?P<path>.*)$', 'django.views.static.serve',
		        {'document_root': '/Users/furmanx/Desktop/oursite/predictions/static', 'show_indexes': True}),
		(r'^users/[0-9]+/site_media/(?P<path>.*)$', 'django.views.static.serve',
				{'document_root': '/Users/furmanx/Desktop/oursite/predictions/static', 'show_indexes': True}),
		(r'^predictions/[0-9]+/site_media/(?P<path>.*)$', 'django.views.static.serve',
				{'document_root': '/Users/furmanx/Desktop/oursite/predictions/static', 'show_indexes': True}),
    )
    