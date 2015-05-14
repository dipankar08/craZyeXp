from django.shortcuts import render, render_to_response
def store_home(request,uid=None):
    return render_to_response('store_home.html');
