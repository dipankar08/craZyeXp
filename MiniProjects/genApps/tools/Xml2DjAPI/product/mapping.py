from django.conf.urls import patterns, include, url
import os
here = lambda x: os.path.join(os.path.abspath(os.path.dirname(__file__)), x)
from . import ajaxHandeler
urlpatterns = patterns('',)
TEMPLATE_DIRS =('',here('templates'),)

urlpatterns += patterns('',
    # Read Operation
    (r'^api/Book/$',ajaxHandeler.ajax_Book),
    (r'^api/Book/(?P<id>\d+)/$',ajaxHandeler.ajax_Book),
    #(r'^Book/$',views.tt_home),
)


urlpatterns += patterns('',
    # Allowing adding and removing tags..
    (r'^api/Book/(?P<id>\d+)/list/$',ajaxHandeler.ajax_Book_list),
    (r'^api/Book/list/$',ajaxHandeler.ajax_Book_list),
)


urlpatterns += patterns('',
    # Allowing advance search
    (r'^api/Book/aq/$',ajaxHandeler.ajax_Book_asearch),
)

