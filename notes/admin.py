from django.contrib import admin

from .models import Note


class NoteAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'title', 'text', 'created_time', 'updated_time']


admin.site.register(Note, NoteAdmin)
from django.contrib import admin

# Register your models here.
