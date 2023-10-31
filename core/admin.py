from django.contrib import admin
from . import models

admin.site.register(models.Speciality)
admin.site.register(models.Tech) 
admin.site.register(models.Ticket)
admin.site.register(models.Criticy)
admin.site.register(models.History)