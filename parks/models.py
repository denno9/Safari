from django.db import models

# Create your models here.
class ParksModel(models.Model):
    title = models.CharField(max_length=120)
    image = models.ImageField(upload_to='photos/%Y/%m/%d')
    subtitle = models.CharField(max_length=300)
    description = models.CharField(max_length=5000)
    top = models.BooleanField(default=False)



    def __str__(self):
        return self.title