#from tabnanny import verbose
from django.db import models

# Create your models here.
class User(models.Model):
    username = models.CharField('Username', max_length=100)
    password = models.CharField('Password', max_length=100)
    first_name = models.CharField('First Name', max_length=100)
    last_name = models.CharField('Last Name', max_length=100)

    class Meta:
        verbose_name = 'Username'
        verbose_name_plural = 'Username'

    def __str__(self):
        return self.user