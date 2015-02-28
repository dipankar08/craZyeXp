import pdb
from django.conf.urls import patterns, include, url
import os
here = lambda x: os.path.join(os.path.abspath(os.path.dirname(__file__)), x)
from . import ajaxHandeler
urlpatterns = patterns('',)
TEMPLATE_DIRS =('',here('templates'),)

urlpatterns += patterns('',
    # Read Operation
    (r'^api/payroll/$',ajaxHandeler.ajax_PayRoll),
    (r'^api/payroll/(?P<id>\d+)/$',ajaxHandeler.ajax_PayRoll),
    #(r'^payroll/$',views.tt_home),
)


urlpatterns += patterns('',
    # Allowing advance search
    (r'^api/payroll/aq/$',ajaxHandeler.ajax_PayRoll_asearch),
)


urlpatterns += patterns('',
    # Allowing Min View
    (r'^api/payroll/mv/$',ajaxHandeler.ajax_PayRoll_min_view),
)


urlpatterns += patterns('',
    # Allowing Min View
    (r'^api/payroll/qs/$',ajaxHandeler.ajax_PayRoll_quick_search),
)

