from django.db import models

class Course(models.Model):
    name = models.CharField(max_length = 100)
    description = models.TextField()
    slug = models.SlugField(unique = True)
    image = models.ImageField(upload_to = "images")

class User(models.Model):
    first_name = models.CharField(max_length = 50)
    last_name = models.CharField(max_length = 50)
    username = models.CharField(max_length = 50, unique = True)
    email = models.EmailField(unique = True)
    password = models.CharField(max_length = 200)
    profile_picture = models.ImageField(upload_to = "profile_pictures")
    rank = models.IntegerField(default = 0) # 0 -> Normal User; 1 -> Teacher (can add courses); 2 -> Administrator