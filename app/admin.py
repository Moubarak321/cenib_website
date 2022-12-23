from django.contrib import admin
from .models import  Cours
# Register your models here.



class AdminCours(admin.ModelAdmin):
    list_display = ['nom']



admin.site.register(Cours, AdminCours )