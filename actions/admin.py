from django.contrib import admin

from .models import Action, Request
# Register your models here.

admin.site.register(Request)
admin.site.register(Action)