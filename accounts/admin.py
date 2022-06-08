from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from accounts.models import User

# Register your models here.
class UserAdmin(UserAdmin):
    list_display = ('register_number','email','phone','user_type')
    filter_horizontal = ()
    ordering = ('register_number',)
    search_fields = ['register_number']
    list_filter = ('user_type','email')
    fieldsets = (
       (None, {'fields': ('email', 'mobile_number','register_number')}),
       ('Permissions', {'fields': ('user_type',)}),
   )
    add_fieldsets = (
       (None, {
           'classes': ('wide',),
           'fields': ('register_number','email','phone','is_active','user_type'),
       }),
   )


admin.site.register(User,UserAdmin)