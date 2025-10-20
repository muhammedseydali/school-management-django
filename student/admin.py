from django.contrib import admin
from .models import Parent, Student

@admin.register(Parent)
class ParentAdmin(admin.ModelAdmin):
    list_display = ('father_name', 'mother_name', 'father_mobile', 'mother_mobile')


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'student_id', 'student_class', 'section', 'gender')
    prepopulated_fields = {'slug': ('first_name', 'last_name', 'student_id')}
    search_fields = ('first_name', 'last_name', 'student_id', 'admission_number')
    list_filter = ('student_class', 'section', 'gender')