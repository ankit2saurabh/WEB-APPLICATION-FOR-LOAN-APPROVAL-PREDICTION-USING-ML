from __future__ import unicode_literals
from django.db import models

# Create your models here.
class News(models.Model):
    name = models.CharField(max_length=50)
    short_txt = models.TextField(max_length=100)
    body_txt = models.TextField()
    date = models.TextField(max_length=12)
    picname = models.TextField()
    picurl = models.TextField(default='-')
    Writer = models.CharField(max_length=50)
    category = models.CharField(max_length=50,default='-')
    categoryid = models.IntegerField(default=0)
    show = models.IntegerField(default=0)

    class Meta:
        verbose_name_plural = 'News'

    def __str__(self):
        return self.name + " | " + str(self.pk)
# Remove teh active class

