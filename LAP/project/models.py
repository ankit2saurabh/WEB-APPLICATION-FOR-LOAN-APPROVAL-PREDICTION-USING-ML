from __future__ import unicode_literals
from django.db import models
from django.db.models.fields import EmailField

# Create your models here.
class Project(models.Model):
    name = models.CharField(max_length=15)
    fb = models.CharField(default='-',max_length=100)
    tw = models.CharField(default='-',max_length=100)
    insta = models.CharField(default='-',max_length=100)
    linkden = models.CharField(default='-',max_length=100)
    gml = models.CharField(default='-',max_length=100)
    set_name = models.CharField(default='-',max_length=20)
    about = models.TextField()
    # models.IntegerField()
    # models.CharField()
    class Meta:
        verbose_name_plural = 'Project'

    def __str__(self):
        return self.set_name + " | " + str(self.pk)
# Remove teh active class

class Services(models.Model):
    iconclass = models.CharField(default='-',max_length=50)
    title = models.CharField(max_length=20)
    serviceBody = models.CharField(default='-',max_length=50)
    buttonlink = models.TextField()
    # models.IntegerField()
    # models.CharField()

    class Meta:
        verbose_name_plural = 'Service'


    def __str__(self):
        return self.title + " | " + str(self.pk)


class Signup(models.Model):
    fname = models.CharField(max_length=30, default='-')
    lname = models.CharField(max_length=100,default='-')
    fathername = models.CharField(max_length=100,default='-')
    dob = models.DateField(max_length=12)
    mobnum = models.IntegerField()
    email = models.CharField(max_length=320, default='-')
    password = models.CharField(max_length=16, default='-')

    class Meta:
        verbose_name_plural = 'Signup'

    def __str__(self):
        return self.fname + self.lname + " | " + str(self.pk)

class contact(models.Model):
    name = models.CharField(max_length=50,default='Admin')
    email = models.CharField(max_length=320, default='-')
    subject = models.CharField(max_length=120, default='-')
    issues = models.TextField(max_length=1000,default='-')

    def __str__(self):
        return self.email + " | " + str(self.pk)

class subscribe(models.Model):
    mail = models.CharField(max_length=320, default='-')

    def __str__(self):
        return self.mail + " | " + str(self.pk)


class eligblity(models.Model):
    fname = models.CharField(max_length=30, default='-')
    lname = models.CharField(max_length=100,default='-')
    email = models.CharField(max_length=320, default='-')
    state = models.CharField(max_length=25, default='-')
    city = models.CharField(max_length=100,default='-')
    zip = models.CharField(max_length=7,default='-')
    gender = models.CharField(max_length=7,default='-')
    Marital = models.CharField(max_length=3,default='-')
    Dependents = models.CharField(max_length=2,default=0)
    profession = models.CharField(max_length=3,default='-')
    education = models.CharField(max_length=13,default='-')
    property = models.CharField(max_length=10,default='-')
    takenLoan = models.CharField(max_length=1,default='-')
    aincome = models.CharField(max_length=10,default='-')
    cincome = models.CharField(max_length=10,default='-')
    loanamount = models.CharField(max_length=10,default='-')
    duration = models.CharField(max_length=4,default='-')
    pan = models.CharField(max_length=8,default='-')

    def __str__(self):
        return self.email + " | " + str(self.pk)
    
    class Meta:
        verbose_name_plural = 'eligblity'


# TODO for images
class imagesdata(models.Model):
    image_name = models.CharField(max_length=320, default='-')
    image_description = models.CharField(max_length=320, default=".jpg")

    def __str__(self):
        return self.image_name + " | " + str(self.pk)