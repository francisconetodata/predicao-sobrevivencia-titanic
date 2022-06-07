from django.contrib import admin

# Register your models here.
from .models import Base

@admin.register(Base)
class BaseAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'survived',
        'embarked'
    )