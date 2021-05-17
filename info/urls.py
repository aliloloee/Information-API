from django.urls import path
from .import views

app_name = 'info'

urlpatterns = [
    path('info', views.post_info, name='info')
]