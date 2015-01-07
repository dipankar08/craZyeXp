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
    #home page 
    #(r'^$',   direct_to_template, {'template': 'home_home.html'}),
    
    # FeedBack Operation 
    (r'^api/feedback/$',ajaxHandeler.ajax_feedback),
    (r'^feedback/$',views.feedback_home),
    #(r'^$',views.feedback_home),
    #(r'^$', TemplateView.as_view(template_name='feedback_home.html'), name="home"),
)

# This balically contains all Dipankar-Homepge related HTML 
from django.views.generic import TemplateView
from django.views.generic import RedirectView
urlpatterns += patterns('',
    url(r'^$', TemplateView.as_view(template_name='home_home.html'), name="home"),
    url(r'^qe/$',RedirectView.as_view(url='/media/html/quickedit_index.html')),
    url(r'^kobita/$', RedirectView.as_view(url='/media/html/kobita.html')),
    url(r'^ts/$', RedirectView.as_view(url='/media/html/tootstrap.html')),
)




# We have Clean code Here, later we have to mode from here ..TODOD
urlpatterns += patterns('',
    (r'^api/cleancode/compile/$',ajaxHandeler.ajax_cleancode_compile),
)




TEMPLATE_DIRS =('',
                here('templates'),
                )
