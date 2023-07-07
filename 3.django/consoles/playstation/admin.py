from django.contrib import admin
from . import models

class ModeloAdmin(admin.ModelAdmin):
    ...

admin.site.register(models.Modelo, ModeloAdmin)

