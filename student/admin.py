from django.contrib import admin
from django.utils.html import format_html
from .models import Parent, Student

@admin.register(Parent)
class ParentAdmin(admin.ModelAdmin):
    list_display = ('father_name', 'mother_name', 'father_mobile', 'mother_mobile')


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = (
        'first_name', 
        'last_name', 
        'student_id', 
        'student_class', 
        'section', 
        'gender', 
        'student_image_tag'
    )
    prepopulated_fields = {'slug': ('first_name', 'last_name', 'student_id')}
    search_fields = ('first_name', 'last_name', 'student_id', 'admission_number')
    list_filter = ('student_class', 'section', 'gender')

    def student_image_tag(self, obj):
        if obj.student_image and hasattr(obj.student_image, 'url'):
            return format_html(
                '<img src="{}" width="50" height="50" style="object-fit:cover; border-radius:50%;" />',
                obj.student_image.url
            )
        return "-"
    student_image_tag.short_description = 'Image'
    student_image_tag.allow_tags = True

