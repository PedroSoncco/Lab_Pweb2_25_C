from django.db import models

# Create your models here.

class Simple(models.Model):
    text = models.CharField(max_length=10)
    number = models.IntegerField(null=True)
    url = models.URLField(default='www.example.com')
    
    def __str__(self):
        return self.url
    
class DataExample(models.Model):
    the_date = models.DataTimeField()

class NullExample(models.Model):
    col = models.CharField(max_length=10, blank=True,null=True)

class Language(models.Model):
    name = models.CharField(max_length=10)

class Framework(models.Model):
    name = models.CharField(max_length=10)
    language = models.ForeignKey(Language, on_delete=models.CASCADE)