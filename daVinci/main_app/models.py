from django.db import models

class Course(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    slug = models.SlugField(unique=True)
    image = models.ImageField(upload_to="images")