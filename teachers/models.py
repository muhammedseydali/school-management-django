from django.db import models
from django.utils.text import slugify

GENDER_CHOICES = (
    ('Male', 'Male'),
    ('Female', 'Female'),
    ('Other', 'Other'),
)

class Teacher(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    teacher_id = models.CharField(max_length=20, unique=True)
    teacher_class = models.CharField(max_length=10, blank=True, null=True)
    section = models.CharField(max_length=5, blank=True, null=True)
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES)
    subject = models.CharField(max_length=50)
    mobile_number = models.CharField(max_length=15)
    address = models.TextField()
    teacher_image = models.ImageField(upload_to='teachers/', blank=True, null=True)
    slug = models.SlugField(unique=True, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(f"{self.first_name}-{self.last_name}-{self.teacher_id}")
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
