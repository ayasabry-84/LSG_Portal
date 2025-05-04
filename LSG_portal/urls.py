"""
URL configuration for LSG_portal project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
# LSG_portal/urls.py

from django.contrib import admin
from django.urls import path, include
from django.contrib.auth.views import LogoutView  # استيراد LogoutView بشكل صحيح
from login_dashboard import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('requests/', include('hr_requests.urls')),
    path('canteen/', include('canteen.urls')),
    path('', views.login_view, name='home'),  # إعادة توجيه المستخدم إلى صفحة تسجيل الدخول
    path('login/', views.login_view, name='login'),
    path('login_dashboard/', include('django.contrib.auth.urls')),  # روابط تسجيل الدخول والخروج
    path('logout/', LogoutView.as_view(), name='logout'),  # رابط الخروج
    path('dashboard/', views.dashboard_view, name='dashboard')
]

from django.conf import settings
from django.conf.urls.static import static

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
