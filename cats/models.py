from django.db import models

# Create your models here.

class Post(models.Model):
        image_cat = models.ImageField()
        name_cat = models.CharField(max_length=30)
        ascii_cat = models.TextField()
        title = models.CharField(max_length=200)
        
        def publish(self):
            self.save()

        def __str__(self):
            return self.title