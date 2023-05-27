from django.db import models


class About (models.Model):
    title=models.CharField(max_length=255)
    description=models.TextField(max_length=255)
    img = models.ImageField(upload_to='About/')
    ExYears=models.IntegerField(unique=True)
    chefs=models.IntegerField(unique=True)
    
    
    def __str__(self):
        return self.title

class About2(models.Model):
    title=models.CharField(max_length=255)
    description=models.TextField(max_length=255)
    img = models.ImageField(upload_to='Chef/')
    facebook=models.CharField(max_length=255,blank=True,null=True)
    twitter=models.CharField(max_length=255,blank=True,null=True)
    instagram=models.CharField(max_length=255,blank=True,null=True)
    class Meta:
        verbose_name_plural='Chef'
    def __str__(self):
        return self.title
    

class Service (models.Model):
    title=models.CharField(max_length=255)
    description=models.TextField(max_length=255)

    def __str__(self):
        return self.title
    
class Menu (models.Model):
    title=models.CharField(max_length=255)
    description=models.CharField(max_length=255)
    retsept=models.CharField(max_length=255)
    stoke=models.FloatField()
    img = models.ImageField(upload_to='Menu/')

    def __str__(self):
        return self.title

        

class Booking (models.Model):
    name = models.CharField(max_length=250)
    email = models.EmailField(max_length=250)
    data =models.CharField(max_length=100)
    people=models.CharField(max_length=255)
    text=models.TextField(max_length=255)

    def __str__(self):
        return self.name
class ContactUs(models.Model):
    name = models.CharField(max_length=250)
    email = models.EmailField(max_length=250)
    subject=models.CharField(max_length=255)
    text = models.TextField()


    def __str__(self):
        return self.name

class Map(models.Model):
    map=models.CharField(max_length=255,blank=True,null=True)

class Vidio(models.Model):
    vidio=models.CharField(max_length=255,blank=True,null=True)

class Clients (models.Model):
    title=models.CharField(max_length=255)
    description=models.TextField(max_length=255)
    stoke=models.CharField(max_length=255)
    img = models.ImageField(upload_to='Clients/', null=True ,blank=True)

    def __str__(self):
        return self.title