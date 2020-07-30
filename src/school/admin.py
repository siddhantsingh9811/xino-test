
from django.contrib import admin
from .models import Reg

class RegAdmin(admin.ModelAdmin):
    pass
admin.site.register(Reg, RegAdmin)