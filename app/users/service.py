from django.http import HttpResponse, HttpRequest

def get_users(request:HttpRequest):
    return HttpResponse('[GET] users')

def post_users(request:HttpRequest):
    return HttpResponse('[POST] users')

def put_users():
    HttpResponse('[PUT] users')

def delete_users():
    HttpResponse('[PATCH] users')