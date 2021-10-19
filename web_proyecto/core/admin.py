from django.contrib import admin
from .models import Portada, Examen

class CoreAdmin(admin.ModelAdmin):
    list_display = ('title', 'order')

admin.site.register(Portada, CoreAdmin)
admin.site.register(Examen, CoreAdmin)


# Register your models here.
