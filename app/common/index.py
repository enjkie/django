from django.urls import path

from app.views import post_greet

def extended_path(route, view, kwargs=None, name=None, method=None):
    if(method != None):
        view = method(view)
    else:
        # view=post_greet(request="dsds")
        print("sdsdadasd")
    return path(route, view, kwargs=kwargs, name=name)