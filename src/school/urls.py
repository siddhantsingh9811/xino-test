from django.urls import path
from django.conf.urls import url

from . import views

app_name = "school"
urlpatterns = [
    path("register/", views.LoginView.as_view(), name="register"),
    
]
