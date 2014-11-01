from django.shortcuts import render, render_to_response
def feedback_home(request,uid=None):
    return render_to_response('feedback_home.html');
