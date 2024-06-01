from django.urls import path # type: ignore
from . import views

app_name = "collatz"
urlpatterns = [
    path("",views.visualize,name="visualize"),
]