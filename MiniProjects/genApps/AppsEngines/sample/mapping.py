import pdb
from django.conf.urls import patterns, include, url
import os
here = lambda x: os.path.join(os.path.abspath(os.path.dirname(__file__)), x)
from . import ajaxHandeler
urlpatterns = patterns('',)
TEMPLATE_DIRS =('',here('templates'),)

urlpatterns += patterns('',
    # Read Operation
    (r'^api/author/$',ajaxHandeler.ajax_Author),
    (r'^api/author/(?P<id>\d+)/$',ajaxHandeler.ajax_Author),
    #(r'^author/$',views.tt_home),
)


urlpatterns += patterns('',
    # Many2 many key Operations
    (r'^api/author/(?P<id>\d+)/book/$',ajaxHandeler.ajax_Author_Book),
)


urlpatterns += patterns('',
    # Allowing adding and removing tags..
    (r'^api/author/(?P<id>\d+)/list/$',ajaxHandeler.ajax_Author_list),
    (r'^api/author/list/$',ajaxHandeler.ajax_Author_list),
)


urlpatterns += patterns('',
    # Allowing advance search
    (r'^api/author/aq/$',ajaxHandeler.ajax_Author_asearch),
)


urlpatterns += patterns('',
    # Allowing Min View
    (r'^api/author/mv/$',ajaxHandeler.ajax_Author_min_view),
)


urlpatterns += patterns('',
    # Allowing Min View
    (r'^api/author/qs/$',ajaxHandeler.ajax_Author_quick_search),
)


urlpatterns += patterns('',
    # Read Operation
    (r'^api/publication/$',ajaxHandeler.ajax_Publication),
    (r'^api/publication/(?P<id>\d+)/$',ajaxHandeler.ajax_Publication),
    #(r'^publication/$',views.tt_home),
)


urlpatterns += patterns('',
    # Many2 many key Operations
    (r'^api/publication/(?P<id>\d+)/book/$',ajaxHandeler.ajax_Publication_Book),
)


urlpatterns += patterns('',
    # Read Operation
    (r'^api/toc/$',ajaxHandeler.ajax_TOC),
    (r'^api/toc/(?P<id>\d+)/$',ajaxHandeler.ajax_TOC),
    #(r'^toc/$',views.tt_home),
)


urlpatterns += patterns('',
    # Many2 many key Operations
    (r'^api/toc/(?P<id>\d+)/book/$',ajaxHandeler.ajax_TOC_Book),
)


urlpatterns += patterns('',
    # Read Operation
    (r'^api/book/$',ajaxHandeler.ajax_Book),
    (r'^api/book/(?P<id>\d+)/$',ajaxHandeler.ajax_Book),
    #(r'^book/$',views.tt_home),
)


urlpatterns += patterns('',
    # Many2 many key Operations
    (r'^api/book/(?P<id>\d+)/publication/$',ajaxHandeler.ajax_Book_Publication),
)


urlpatterns += patterns('',
    # Many2 many key Operations
    (r'^api/book/(?P<id>\d+)/toc/$',ajaxHandeler.ajax_Book_TOC),
)


urlpatterns += patterns('',
    # Many2 many key Operations
    (r'^api/book/(?P<id>\d+)/author/$',ajaxHandeler.ajax_Book_Author),
)

