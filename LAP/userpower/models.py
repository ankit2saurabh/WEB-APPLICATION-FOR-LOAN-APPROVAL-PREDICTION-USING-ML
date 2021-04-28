from __future__ import unicode_literals
from django.db import models

# Create your models here.
class Control(models.Model):
    name = models.CharField(max_length=50)
    class Meta:
        verbose_name_plural = 'User Control'

    def __str__(self):
        return self.name + " | " + str(self.pk)
# Remove the active class