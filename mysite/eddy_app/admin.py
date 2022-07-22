from django.contrib import admin
from .models import Company

# Register your models here.

class CompanyAdmin(admin.ModelAdmin):
    search_fields = ['company','code']

admin.site.register(Company,CompanyAdmin)