from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import VelNoteUser

class VelNoteUserAdmin(UserAdmin):
    model = VelNoteUser
    list_display = ('email', 'username', 'is_active', 'is_staff')
    list_filter = ('is_active', 'is_staff')
    ordering = ('email',)
    search_fields = ('email', 'username')

admin.site.register(VelNoteUser, VelNoteUserAdmin)
