from django.db import models
from autoslug import AutoSlugField


# Create your models here.
class Categories(models.Model):
    name=models.CharField(max_length=200)
    image = models.ImageField(upload_to='categories/',default='')
    def __str__(self):
        return self.name

class Host(models.Model):
    user_name = models.CharField(max_length=200)
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    avatar = models.ImageField(upload_to='host/avatar/',default='')

    def __str__(self):
        return self.user_name

class Properties(models.Model):
    host = models.ForeignKey(Host,on_delete=models.SET_NULL,null=True)
    name = models.CharField(max_length=300)
    property_type = models.ForeignKey(Categories,on_delete=models.SET_NULL,null=True)
    location = models.CharField(max_length=200)
    rooms = models.IntegerField()
    price = models.IntegerField()
    thumbnail = models.ImageField(upload_to='properties/thubnail/',default='')

    def __str__(self):
        return self.name

class Places(models.Model):
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=500)
    thumbnail = models.ImageField(upload_to='places/thumbnail/',default='')
    slug = AutoSlugField(populate_from='name',null=True,default=None)

    def __str__(self):
        return self.name
    

    

    