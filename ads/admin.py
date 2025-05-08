from django.contrib import admin
from .models import *

@admin.register(Ad)
class Admin(admin.ModelAdmin):
    pass