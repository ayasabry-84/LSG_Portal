from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required, user_passes_test
from rest_framework import viewsets
from .models import Meal
from .serializers import MealSerializer
from .forms import MealForm

# دالة التحقق من صلاحية HR أو Admin
def check_hr_admin(user):
    return user.groups.filter(name__in=['HR', 'Admin']).exists() or user.is_superuser

# API ViewSet
class MealViewSet(viewsets.ModelViewSet):
    queryset = Meal.objects.all()
    serializer_class = MealSerializer

# عرض قائمة الوجبات
@login_required
def meal_list(request):
    meals = Meal.objects.all().order_by('name')
    context = {
        'meals': meals,
        'is_hr_admin': check_hr_admin(request.user)
    }
    return render(request, 'canteen/meal_list.html', context)

# عرض تفاصيل الوجبة
@login_required
def meal_detail(request, pk):
    meal = get_object_or_404(Meal, pk=pk)
    context = {
        'meal': meal,
        'is_hr_admin': check_hr_admin(request.user)
    }
    return render(request, 'canteen/meal_detail.html', context)

# إضافة وجبة جديدة (لـ HR/Admin فقط)
@login_required
@user_passes_test(check_hr_admin, login_url='/accounts/login/')
def add_meal(request):
    if request.method == 'POST':
        form = MealForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('meal_list')
    else:
        form = MealForm()
    return render(request, 'canteen/meal_form.html', {
        'form': form,
        'title': 'Add Meal',
        'is_hr_admin': check_hr_admin(request.user)
    })
# تعديل وجبة (لـ HR/Admin فقط)
@login_required
@user_passes_test(check_hr_admin, login_url='/accounts/login/')
def edit_meal(request, pk):
    meal = get_object_or_404(Meal, pk=pk)
    if request.method == 'POST':
        form = MealForm(request.POST, request.FILES, instance=meal)
        if form.is_valid():
            form.save()
            return redirect('meal_detail', pk=meal.pk)
    else:
        form = MealForm(instance=meal)
    return render(request, 'canteen/meal_form.html', {
        'form': form,
        'title': 'Edit Meal',
        'is_hr_admin': check_hr_admin(request.user)
    })

@login_required
@user_passes_test(check_hr_admin, login_url='/accounts/login/')
def delete_meal(request, pk):
    meal = get_object_or_404(Meal, pk=pk)
    if request.method == 'POST':
        meal.delete()
        return redirect('meal_list')
    return render(request, 'canteen/meal_confirm_delete.html', {
        'meal': meal,
        'is_hr_admin': check_hr_admin(request.user)
    })