from django.db import models

# Create your models here.

    

class Post(models.Model):
    image = models.ImageField(upload_to="Post/")
    full_name = models.CharField(max_length=250)
    

    
    def __str__(self):
        return self.full_name
    

class Contact(models.Model):
    name=models.CharField(max_length=255)
    email=models.EmailField()
    title=models.CharField(max_length=255)
    description=models.TextField()

    def __str__(self):
        return self.name
      