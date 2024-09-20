from django.shortcuts import render
from django.http import HttpResponse, HttpRequest
from django.views.decorators.csrf import csrf_exempt
from .common.decorators import post

def greet(request: HttpRequest):
    query = request.GET.dict()
    name, age = query["name"], query["age"]
    return HttpResponse(f"Hello, {name} of age:{age}")
# @csrf_exempt
def post_greet(request:HttpRequest):
    print("dasdaskdsa")
    return HttpResponse(f"Hello")