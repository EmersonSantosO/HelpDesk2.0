from django.db import models
from django.contrib.auth.models import User


class Tech(models.Model):
    first_name = models.CharField(max_length=100, verbose_name="Nombre")
    last_name = models.CharField(max_length=100, verbose_name="Apellidos")
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self) -> str:
        return self.first_name

class Ticket(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    tech = models.ForeignKey(Tech, null=True, blank=True, on_delete=models.RESTRICT)

    def __str__(self) -> str:
        return self.title

    