from django.db import models

# Create your models here.
class landscapes(models.Model): 

    img = models.ImageField(upload_to='pics')


class Phones(models.Model): 

    img = models.ImageField(upload_to='pics')


class Beaches(models.Model): 

    img = models.ImageField(upload_to='pics')


class Houses(models.Model): 

    img = models.ImageField(upload_to='pics')
