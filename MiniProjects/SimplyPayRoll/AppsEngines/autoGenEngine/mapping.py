from django.conf.urls import patterns, include, url
import os
here = lambda x: os.path.join(os.path.abspath(os.path.dirname(__file__)), x)
from . import ajaxHandeler
urlpatterns = patterns('',
    # Read Operation
    (r'^api/Student/$',ajaxHandeler.ajax_Student),
    (r'^api/Student/(?P<id>\d+)/$',ajaxHandeler.ajax_Student),
    #(r'^Student/$',views.tt_home),
)
TEMPLATE_DIRS =('',
                here('templates'),
                )
