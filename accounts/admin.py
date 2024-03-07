from django.contrib import admin
from .models import Account
from django.contrib.auth.admin import UserAdmin

# Register your models here.
class AccouuntAdmin(UserAdmin):
    list_display=('email','first_name','last_name','last_login','date_joined','username','is_active')
    list_display_links=('email', 'first_name', 'last_name')
    readonly_fields=('date_joined', 'last_login')
    ordering=('-date_joined',)

    filter_horizontal=()
    list_filter=()
    fieldsets=()

admin.site.register(Account,AccouuntAdmin)