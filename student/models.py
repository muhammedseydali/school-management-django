from django.db import models

# Create your models here.
class Parent(models.Model):
    father_name = models.CharField(max_length=100)
    father_occuppation = models.CharField(max_length=100)
    father_mobile = models.CharField(max_length=100)
    father_email = models.EmailField(max_length=100)
    mother_name = models.CharField(max_length=100)
    mother_email = models.EmailField(max_length=100)
    mother_mobile = models.CharField(max_length=100)
    present_address = models.TextField()
    permanent_address = models.TextField()

    def __str__(self):
        return f"{self.father_name} & {self.mother_name}"