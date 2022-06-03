from django.urls import path
from . import views
from .views import *
import mainpage.views

urlpatterns = [
    path('main/', views.main, name='main'),
]