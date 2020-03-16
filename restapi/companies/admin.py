from django.contrib import admin

# Register your models here.
from companies.models import Stock

admin.site.register(Stock)