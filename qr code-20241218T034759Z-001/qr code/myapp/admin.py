from django.contrib import admin
from myapp.models import *
from django.contrib.auth.admin import UserAdmin

# Register your models here.

# admin.site.register(FormData)
# admin.site.register(myuser,UserAdmin)

class CustomUserAdmin(UserAdmin):
    list_display = ('username', 'email','qr_code')

admin.site.register(myuser, CustomUserAdmin)

