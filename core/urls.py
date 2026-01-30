from django.urls import path
from . import views

app_name = 'core'

urlpatterns = [
    path('', views.hello, name='home'),
    path('hello/', views.hello, name='hello'),
]
