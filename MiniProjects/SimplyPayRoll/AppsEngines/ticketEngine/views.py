from django.shortcuts import render, render_to_response
def tt_home(request,uid=None):
    return render_to_response('tt_home.html');
