import pdb
from django.conf.urls import patterns, include, url
import os
here = lambda x: os.path.join(os.path.abspath(os.path.dirname(__file__)), x)
from . import ajaxHandeler
from . import views
urlpatterns = patterns('',)
TEMPLATE_DIRS =('',here('templates'),)

urlpatterns += patterns('',
    # Read Operation
    (r'^api/user/$',ajaxHandeler.ajax_User),
    (r'^api/user/(?P<id>\d+)/$',ajaxHandeler.ajax_User),
    #(r'^user/$',views.tt_home),
)


urlpatterns += patterns('',
    # Allowing advance search
    (r'^api/user/aq/$',ajaxHandeler.ajax_User_asearch),
)


urlpatterns += patterns('',
    # Allowing Min View
    (r'^api/user/mv/$',ajaxHandeler.ajax_User_min_view),
)


urlpatterns += patterns('',
    # Allowing Min View
    (r'^api/user/qs/$',ajaxHandeler.ajax_User_quick_search),
)

####################  CUSTOM MAPPING ###############################
urlpatterns += patterns('',
    url(r'^log/$', views.home, name='home'),
    url(r'^login/(\w*)', views.login, name='login')
)
