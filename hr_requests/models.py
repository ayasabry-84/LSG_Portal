from django.db import models

REQUEST_TYPES = [
    ('salary', 'خطاب مفردات المرتب'),
    ('health_insurance', 'خطاب تأمين صحي'),
    ('social_insurance', 'خطاب تأمين اجتماعي'),
    ('vacation', 'طلب اجازة'),
]

class HRRequest(models.Model):
    employee_name = models.CharField(max_length=100)
    employee_id = models.CharField(max_length=50)
    request_type = models.CharField(max_length=20, choices=REQUEST_TYPES)
    photo = models.ImageField(upload_to='vacation_photos/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.employee_name} - {self.get_request_type_display()}"