from django.urls import include
from .views import greet, post_greet
from .common.index import extended_path
from .common.decorators import post
from app.common.router import Router

urlpatterns = [
    extended_path("post_greet", post_greet),
    extended_path("users", include(Router.post), method=post)
]