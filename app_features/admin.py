from django.contrib import admin
from app_features.models import Features

# Register your models here.

class FeaturesAdmin(admin.ModelAdmin):
    list_display = ['title', 'price']
    search_fields = ['title']
    

admin.site.register(Features, FeaturesAdmin)
