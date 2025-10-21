from django.contrib import admin
from .models import Teacher

@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    list_display = (
        'first_name',
        'last_name',
        'teacher_id',
        'subject',
        'teacher_class',
        'section',
        'gender',
        'mobile_number',
        'created_at',
    )
    list_filter = ('gender', 'subject', 'teacher_class', 'section', 'created_at')
    search_fields = ('first_name', 'last_name', 'teacher_id', 'subject', 'mobile_number')
    prepopulated_fields = {'slug': ('first_name', 'last_name', 'teacher_id')}
    readonly_fields = ('created_at', 'updated_at')
    ordering = ('first_name',)
    list_per_page = 20

    fieldsets = (
        ('Personal Info', {
            'fields': ('first_name', 'last_name', 'gender', 'teacher_image')
        }),
        ('Professional Details', {
            'fields': ('teacher_id', 'subject', 'teacher_class', 'section')
        }),
        ('Contact Info', {
            'fields': ('mobile_number', 'address')
        }),
        ('Metadata', {
            'fields': ('slug', 'created_at', 'updated_at')
        }),
    )
