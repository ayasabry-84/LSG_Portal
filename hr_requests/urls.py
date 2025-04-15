# hr_requests/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('', views.request_options_view, name='request_options'),
    path('<str:request_type>/', views.make_request_view, name='make_request'),
]
