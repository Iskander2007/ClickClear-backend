from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import User

@admin.register(User)
class UserAdmin(BaseUserAdmin):
    # Какие поля показывать в списке
    list_display = ("id", "email", "name", "role", "is_active", "is_staff")
    list_filter = ("role", "is_active", "is_staff")
    search_fields = ("email", "name")
    ordering = ("id",)

    # Поля, доступные для редактирования
    fieldsets = (
        (None, {"fields": ("email", "password", "name", "role", "phone", "default_address")}),
        ("Дополнительно", {"fields": ("entrance", "floor", "intercom", "iin", "avatar_url", "rating", "balance", "email_verified", "working_districts")}),
        ("Права доступа", {"fields": ("is_active", "is_staff", "is_superuser", "groups", "user_permissions")}),
    )

    # Поля при создании нового пользователя через админку
    add_fieldsets = (
        (None, {
            "classes": ("wide",),
            "fields": ("email", "name", "password1", "password2", "role", "is_staff", "is_superuser"),
        }),
    )

    readonly_fields = ("rating", "balance")
