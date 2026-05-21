from django.contrib import admin
from .models import user
# Register your models here.
@admin.register(user)
class user_admin(admin.ModelAdmin):
    list_display = ['name', 'age', 'city']