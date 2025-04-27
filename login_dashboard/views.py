from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import user_passes_test
from .models import CustomUser  # تأكدي من استيراد الـ CustomUser من الملف الصحيح

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
        job_id = request.POST['job_id']  # أخذ الرقم الوظيفي من النموذج
        password = request.POST['password']
        user = authenticate(request, job_id=job_id, password=password)  # استخدام job_id بدلاً من username
        if user is not None:
            login(request, user)
            return redirect('dashboard')  # توجيه المستخدم إلى لوحة الـ Dashboard
        else:
            return render(request, 'login.html', {'error': 'Invalid credentials'})  # رسالة الخطأ
    return render(request, 'login.html')

# عرض بيانات المستخدم في الـ Dashboard
def dashboard_view(request):
    user = request.user  # الحصول على بيانات المستخدم الحالي
    return render(request, 'dashboard.html', {'user': user}) 