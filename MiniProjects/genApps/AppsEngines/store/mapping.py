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
from . import views,ajaxHandeler
from django.views.generic import TemplateView
from django.views.generic import RedirectView


import os
here = lambda x: os.path.join(os.path.abspath(os.path.dirname(__file__)), x)



# Urls Controllers ..
urlpatterns = patterns('',
    #(r'^store/$',views.store_home),
    #(r'^store/(?P<path>.*)$',views.myfiles_page), 
    (r'^store/(?P<path>.*\..*)$',views.downloadFile), 
)




TEMPLATE_DIRS =('',here('templates'), )
