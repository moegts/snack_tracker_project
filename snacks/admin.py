from django.contrib import admin
from .models import Snacks
# Register your models here.

# @admin.register(Snacks)

# class AdminSnacks(admin.ModelAdmin):
#     list_display = ['name', 'purchaser']

admin.site.register(Snacks)