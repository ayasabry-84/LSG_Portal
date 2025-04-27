from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register(r'meals', views.MealViewSet)

urlpatterns = [
    # API endpoints
    path('api/', include(router.urls)),
    
    # Web views
    path('', views.meal_list, name='meal_list'),
    path('meal/<int:pk>/', views.meal_detail, name='meal_detail'),
    path('add/', views.add_meal, name='add_meal'),
    path('edit/<int:pk>/', views.edit_meal, name='edit_meal'),
    path('delete/<int:pk>/', views.delete_meal, name='delete_meal'),
]