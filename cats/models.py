from django.db import models

# Create your models here.

class Cats(models.Model):
        # image_cat = models.ImageField()
        name_cat = models.CharField(max_length=30)
        ascii_cat = models.TextField()
        desc_cat = models.CharField(max_length=200)
        imagen_cat = models.ImageField(upload_to="cats", null=True)

        def __str__(self):
            return self.name_cat