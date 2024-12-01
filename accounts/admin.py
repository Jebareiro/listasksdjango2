from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import CustomUser

class UserAdmin(BaseUserAdmin):
    # Cambié 'username' por 'email' porque 'username' no existe en tu modelo
    list_display = (
        "email",  # Usamos 'email' en lugar de 'username'
        "is_active",
        "is_staff",
        "is_superuser",
    )

    # Añadí 'email' y 'password' en lugar de 'username'
    add_fieldsets = (
        (None, {
            'fields': (
                'email',  # Usamos 'email' en lugar de 'username'
                'password1',
                'password2',
            )}
        ),
    )

    # Añadí 'email' y 'age' en lugar de 'username'
    fieldsets = (
        (None, {'fields': (
            'email',  # Usamos 'email' en lugar de 'username'
            'age',
            'password'
        )}),
        ('Permissions', {'fields': (
            'is_active',
            'is_staff',
            'is_superuser',
            'groups',
            'user_permissions'
        )}),
    )

    # Usamos 'email' para la búsqueda, ya que 'username' no existe
    search_fields = ('email',)

    # También puedes ordenar por 'email' en lugar de 'username'
    ordering = ('email',)

admin.site.register(CustomUser, UserAdmin)
