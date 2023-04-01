from django.contrib import admin

from .models import Auto


class AutoAdmin(admin.ModelAdmin):
    list_display = ['car_model']
    list_filter = ['car_model']
    list_display_links = ['car_model']


admin.site.register(Auto, AutoAdmin)
