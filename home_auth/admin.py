from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser, PasswordResetRequest

# Custom admin for your CustomUser
class CustomUserAdmin(UserAdmin):
    model = CustomUser
    list_display = ('username', 'email', 'first_name', 'last_name', 'is_student', 'is_teacher', 'is_admin', 'is_authorized', 'date_joined')
    list_filter = ('is_student', 'is_teacher', 'is_admin', 'is_authorized')
    search_fields = ('username', 'email', 'first_name', 'last_name')
    ordering = ('date_joined',)
    fieldsets = (
        (None, {'fields': ('username', 'email', 'password')}),
        ('Personal Info', {'fields': ('first_name', 'last_name')}),
        ('Permissions', {'fields': ('is_student', 'is_teacher', 'is_admin', 'is_authorized', 'groups', 'user_permissions')}),
        ('Important dates', {'fields': ('last_login', 'date_joined')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'email', 'password1', 'password2', 'first_name', 'last_name', 'is_student', 'is_teacher', 'is_admin', 'is_authorized')}
        ),
    )

# Admin for PasswordResetRequest
class PasswordResetRequestAdmin(admin.ModelAdmin):
    list_display = ('user', 'email', 'token', 'created_at')
    search_fields = ('user__username', 'email', 'token')
    readonly_fields = ('token', 'created_at')
    ordering = ('-created_at',)

# Register models
admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(PasswordResetRequest, PasswordResetRequestAdmin)
