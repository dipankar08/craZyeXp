from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'sampleProject.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
)
############  read static files #######################
from sampleProject import settings
if settings.DEBUG:
    urlpatterns += patterns('',
        (r'^media/(?P<path>.*)$', 'django.views.static.serve',
             {'document_root':     settings.STATIC_ROOT}),
    )

################ Adding urls from AppEngines by Auto detected #######
from django.conf.urls import include
from settings import ListHelperEngine
for engine in ListHelperEngine:
    urlpatterns += patterns('',
        url(r'', include('AppsEngines.'+engine[0]+'.mapping')),
    )

