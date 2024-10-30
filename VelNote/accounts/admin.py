from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import VelNoteUser

class VelNoteUserAdmin(UserAdmin):
    model = VelNoteUser
    list_display = ('email', 'username', 'is_active', 'is_staff')
    list_filter = ('is_active', 'is_staff')
    ordering = ('email',)
    search_fields = ('email', 'username')
    
    fieldsets = (
     (None, {'fields': ('username', 'password')}),
     ('Personal info', {'fields': ('email',)}),  # Removed profile_picture
     ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
     ('Important dates', {'fields': ('last_login',)}), 
    )


admin.site.register(VelNoteUser, VelNoteUserAdmin)
