from django.urls import path
from . import views

urlpatterns = [
    path('hello/', views.say_hello)
    #useless comment
    #after opening template branch
    ]