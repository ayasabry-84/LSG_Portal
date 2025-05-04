from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import user_passes_test, login_required
from django.contrib import messages
from .models import CustomUser  # تأكدي إنه فعلاً ده اسم الموديل

# دالة للتحقق من كون المستخدم هو المشرف
def is_admin(user):
    return user.is_superuser

# لوحة تحكم للمشرفين فقط
@user_passes_test(is_admin)
def admin_dashboard(request):
    users = CustomUser.objects.all()  # عرض كل المستخدمين
    return render(request, 'admin_dashboard.html', {'users': users})

# دالة لتسجيل الدخول
def login_view(request):
    if request.method == 'POST':
        job_id = request.POST['job_id']
        password = request.POST['password']
        
        # التأكد من صحة البيانات
        user = authenticate(request, job_id=job_id, password=password)  
        
        if user is not None:
            login(request, user)
            return redirect('dashboard')
        else:
            messages.error(request, "رقم الوظيفة أو كلمة المرور غير صحيحة")
            return redirect('login')  # إعادة التوجيه لنفس الصفحة
    return render(request, 'login.html')

# عرض بيانات المستخدم في الـ Dashboard
@login_required
def dashboard_view(request):
    return render(request, 'dashboard.html', {'user': request.user})