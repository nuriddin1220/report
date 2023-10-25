from django.urls import path
from .views import home,reports,passwords,analysis,myreports

urlpatterns = [
    path('',home,name='home'),
    path('reports/',reports,name='reports'),
    path('passwords/',passwords,name='passwords'),
    path('analysis/',analysis,name='analysis'),
    path('myreports/',myreports,name='myreports'),
    
]
