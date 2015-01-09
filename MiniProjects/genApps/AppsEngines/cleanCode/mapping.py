import pdb
from django.conf.urls import patterns, include, url
import os
here = lambda x: os.path.join(os.path.abspath(os.path.dirname(__file__)), x)
from . import ajaxHandeler
urlpatterns = patterns('',)
TEMPLATE_DIRS =('',here('templates'),)

urlpatterns += patterns('',
    # Read Operation
    (r'^api/code/$',ajaxHandeler.ajax_Code),
    (r'^api/code/(?P<id>\d+)/$',ajaxHandeler.ajax_Code),
    #(r'^code/$',views.tt_home),
)


urlpatterns += patterns('',
    # Allowing adding and removing tags..
    (r'^api/code/(?P<id>\d+)/list/$',ajaxHandeler.ajax_Code_list),
    (r'^api/code/list/$',ajaxHandeler.ajax_Code_list),
)


urlpatterns += patterns('',
    # Allowing advance search
    (r'^api/code/aq/$',ajaxHandeler.ajax_Code_asearch),
)


urlpatterns += patterns('',
    # Allowing Min View
    (r'^api/code/mv/$',ajaxHandeler.ajax_Code_min_view),
)


urlpatterns += patterns('',
    # Allowing Min View
    (r'^api/code/qs/$',ajaxHandeler.ajax_Code_quick_search),
)

