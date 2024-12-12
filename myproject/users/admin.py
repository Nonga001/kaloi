from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User

class CustomUserAdmin(UserAdmin):
    model = User
    list_display = ['username', 'email', 'first_name', 'last_name', 'get_role']

    def get_role(self, obj):
        # Get the user's group to determine the role
        if obj.groups.filter(name='students').exists():
            return 'Student'
        elif obj.groups.filter(name='lecturers').exists():
            return 'Lecturer'
        return 'None'
    get_role.short_description = 'Role'

admin.site.register(User, CustomUserAdmin)
