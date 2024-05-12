from django.contrib import admin

from .models import Account


class UserAdmin(admin.ModelAdmin):
    list_display = ['id', 'username', 'created_time']


admin.site.register(Account, UserAdmin)