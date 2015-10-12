from django.conf.urls import patterns, include, url
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'genApps.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
)
############  read static files #######################
from genApps import settings

urlpatterns += patterns('',
    (r'^media/(?P<path>.*)$', 'django.views.static.serve',
         {'document_root':     settings.STATIC_ROOT}),
)

################ Adding urls from AppEngines by Auto detected #######
from django.conf.urls import include
from django.views.generic import TemplateView
from settings import ListHelperEngine
for engine in ListHelperEngine:
  if engine:
    print 'Loading Engine:',engine
    urlpatterns += patterns('',
        url(r'', include('AppsEngines.'+engine[0]+'.mapping')),
    )

urlpatterns += patterns('',
     #  url(r'^$', TemplateView.as_view(template_name='index.html'), name="home"),
      ) 
if settings.IS_PRODUCTION:
    from django.shortcuts import render_to_response
    from django.template import RequestContext
    def handler404(request):
        response = render_to_response('404.html', {},
                                      context_instance=RequestContext(request))
        response.status_code = 404
        return response

    def handler500(request):
        response = render_to_response('500.html', {},
                                      context_instance=RequestContext(request))
        response.status_code = 500
        return response
