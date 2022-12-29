from django.contrib import admin
from .models import  Cours, Favorite, Formateur
# Register your models here.



class AdminCours(admin.ModelAdmin):
    list_display = ['nom']



admin.site.register(Cours, AdminCours )
admin.site.register(Favorite)
admin.site.register(Formateur)