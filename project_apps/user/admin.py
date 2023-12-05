from django.contrib import admin

from .models import FlxFitUser
# Register your models here.
@admin.register(FlxFitUser)
class FlxFitUserAdmin(admin.ModelAdmin):
    verbose_name = "Flx Fit User"