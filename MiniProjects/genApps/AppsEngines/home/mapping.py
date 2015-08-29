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
    url(r'^chat/$', RedirectView.as_view(url='/media/unitTest/websocket1.html')),
    #url(r'^cleancode/$', RedirectView.as_view(url='/media/html/cleanCode_r.html')),
)




###################  CLEAN CODE   #####################################
urlpatterns += patterns('',
    (r'^api/cleancode/compile/$',ajaxHandeler.ajax_cleancode_compile),
    (r'^api/cleancode/run/$',ajaxHandeler.ajax_cleancode_run),
    (r'^api/cleancode/perf/$',ajaxHandeler.ajax_cleancode_perf),
    (r'^cleancode/$',ajaxHandeler.edit_file),
    (r'^cleancode/(?P<id>\d+)/$',ajaxHandeler.edit_file),
    (r'^api/cleancode/(?P<id>\d+)/download/$',ajaxHandeler.download_file),
    (r'^api/cleancode/(?P<id>\d+)/view/$',ajaxHandeler.view_file),
    (r'^cleancode/(?P<id>\d+)/iview/$',ajaxHandeler.iview_file),
    (r'^cleancode/(?P<id>\d+)/iview/save/$',ajaxHandeler.iview_file_save),    
    (r'^cleancode/(?P<id>\d+)/look/$',ajaxHandeler.look),
    (r'^api/cleancode/book/$',ajaxHandeler.view_book),
    (r'^api/cleancode/stat/$',ajaxHandeler.get_stat),
    (r'^api/cleancode/buildBooklet/$',ajaxHandeler.buildBooklet),
    (r'^api/email/$',ajaxHandeler.ajax_send_email),
)

###################  YOUTUBE   #####################################
urlpatterns += patterns('',
    (r'^youtube/$',ajaxHandeler.ajax_youtube)
    )

###################  SOCIAL AUTH   #####################################
urlpatterns += patterns('',
    url(r'^log/$', views.home, name='home'),
    url(r'^login/(\w*)', views.login, name='login')
)


TEMPLATE_DIRS =('',
                here('templates'),
                )
