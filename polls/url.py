from . import views
from django.urls import path

urlpatterns = [
    
    path('',views.polls,name='poll_poll')
    
]
