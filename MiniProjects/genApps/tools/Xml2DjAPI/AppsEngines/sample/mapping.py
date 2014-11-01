from django.conf.urls import patterns, include, url
import os
here = lambda x: os.path.join(os.path.abspath(os.path.dirname(__file__)), x)
from . import ajaxHandeler
urlpatterns = patterns('',)
TEMPLATE_DIRS =('',here('templates'),)

urlpatterns += patterns('',
    # Read Operation
    (r'^api/Author/$',ajaxHandeler.ajax_Author),
    (r'^api/Author/(?P<id>\d+)/$',ajaxHandeler.ajax_Author),
    #(r'^Author/$',views.tt_home),
)


urlpatterns += patterns('',
    # Allowing adding and removing tags..
    (r'^api/Author/(?P<id>\d+)/list/$',ajaxHandeler.ajax_Author_list),
    (r'^api/Author/list/$',ajaxHandeler.ajax_Author_list),
)


urlpatterns += patterns('',
    # Allowing advance search
    (r'^api/Author/aq/$',ajaxHandeler.ajax_Author_asearch),
)


urlpatterns += patterns('',
    # Read Operation
    (r'^api/Publication/$',ajaxHandeler.ajax_Publication),
    (r'^api/Publication/(?P<id>\d+)/$',ajaxHandeler.ajax_Publication),
    #(r'^Publication/$',views.tt_home),
)


urlpatterns += patterns('',
    # Read Operation
    (r'^api/Book/$',ajaxHandeler.ajax_Book),
    (r'^api/Book/(?P<id>\d+)/$',ajaxHandeler.ajax_Book),
    #(r'^Book/$',views.tt_home),
)


urlpatterns += patterns('',
    # Many2 many key Operations
    (r'^api/Book/(?P<id>\d+)/Author/$',ajaxHandeler.ajax_Book_Author),
)

