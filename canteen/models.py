# canteen/models.py
from django.db import models

class Meal(models.Model):
    name = models.CharField(max_length=100, verbose_name="Meal Name")  # اسم الوجبة
    description = models.TextField(default="No description", verbose_name="Description")  # وصف الوجبة
    price = models.DecimalField(max_digits=5, decimal_places=2, verbose_name="Price")  # سعر الوجبة
    time = models.TimeField(verbose_name="Serving Time")  # وقت تقديم الوجبة (الفطور/الغداء/العشاء)
    image = models.ImageField(upload_to='meal_images/', blank=True, null=True, verbose_name="Image")  # صورة الوجبة

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Meal"
        verbose_name_plural = "Meals"
        ordering = ['name']