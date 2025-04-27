from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.db import models

class CustomUserManager(BaseUserManager):
    def create_user(self, job_id, password=None, **extra_fields):
        if not job_id:
            raise ValueError("يجب إدخال الرقم الوظيفي")
        # إنشاء المستخدم باستخدام الرقم الوظيفي
        user = self.model(job_id=job_id, **extra_fields)
        user.set_password(password)  # تعيين كلمة المرور بشكل مشفر
        user.save(using=self._db)  # حفظ المستخدم
        return user

    def create_superuser(self, job_id, password=None, **extra_fields):
        # تعيين الحقول الافتراضية للمشرف
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)  # تأكد من تفعيل حساب المشرف

        # إنشاء superuser باستخدام نفس الطريقة لإنشاء مستخدم عادي
        return self.create_user(job_id, password, **extra_fields)

class CustomUser(AbstractBaseUser, PermissionsMixin):
    job_id = models.CharField(max_length=20, unique=True)  # الرقم الوظيفي
    full_name = models.CharField(max_length=100)  # الاسم الكامل
    department = models.CharField(max_length=100, blank=True)  # القسم
    birth_date = models.DateField(null=True, blank=True)  # تاريخ الميلاد

    # حقول الصلاحيات
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = CustomUserManager()

    # تحديد اسم المستخدم سيكون الرقم الوظيفي
    USERNAME_FIELD = 'job_id'
    REQUIRED_FIELDS = ['full_name']  # الحقول المطلوبة عند إضافة مستخدم جديد

    def __str__(self):
        return f"{self.full_name} ({self.job_id})"