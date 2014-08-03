########################################################################################
## Author : Dipankar Dutta
## Title :
## Description:
## Function: Just a replacement of urls.py to extend to plag and play with this apps.
##          - You donot need to worries how it works
##          - you just need to add the following urls and TEMPLATE_DIR.
##          - Great na !
#########################################################################################

from django.conf.urls import patterns, include, url

import os
here = lambda x: os.path.join(os.path.abspath(os.path.dirname(__file__)), x)



from . import views,ajaxHandeler
urlpatterns = patterns('',
    # Read Operation
    (r'^api/tt/$',ajaxHandeler.ajax_TT),
    (r'^api/tt/(?P<tid>\d+)/$',ajaxHandeler.ajax_TT),
    (r'^api/tt/(?P<tid>\d+)/changeState$',ajaxHandeler.ajax_changeState),
    (r'^api/tt/(?P<tid>\d+)/comment$',ajaxHandeler.ajax_commentOnTT),
    (r'^api/tt/(?P<tid>\d+)/history$',ajaxHandeler.ajax_getTTHistory),
    (r'^tt/$',views.tt_home),
)

TEMPLATE_DIRS =('',
                here('templates'),
                )
