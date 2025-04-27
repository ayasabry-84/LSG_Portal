from django.urls import path
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('logout/', LogoutView.as_view(), name='logout'),  # رابط لتسجيل الخروج
]