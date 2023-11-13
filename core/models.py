from django.db import models
from django.contrib.auth.models import User

class Criticy(models.Model):
    level = models.CharField(verbose_name="level",max_length=50)

    def __str__(self) -> str:
        return self.level



class Tech(models.Model):
    name = models.CharField(verbose_name="Name",max_length=50)
    last_name = models.CharField(verbose_name="Last Name",max_length=50)

    user = models.OneToOneField(User,verbose_name="User",on_delete=models.CASCADE,null=True,blank=True)
    def __str__(self) -> str:
        return self.name




class Ticket(models.Model):
    title = models.CharField(verbose_name="Title", max_length=50)
    description = models.TextField(verbose_name="Description")
    created_at = models.DateTimeField(auto_now_add=True,verbose_name="Created at")
    updated_at = models.DateTimeField(auto_now=True,verbose_name="Update at")
    tech = models.ForeignKey(Tech,verbose_name="Tech",on_delete=models.SET_NULL,null=True,blank=True)
    criticy = models.ForeignKey(Criticy,verbose_name="Criticy",on_delete=models.SET_NULL,null=True,blank=True)
    
    def __str__(self) -> str:
        return self.title





    