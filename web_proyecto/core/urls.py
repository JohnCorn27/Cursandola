from django.urls import path
from . import views
from .views import inicio

urlpatterns = [
    path('', inicio.as_view(), name="home"),

]