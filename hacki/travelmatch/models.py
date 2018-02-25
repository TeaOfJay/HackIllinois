from django.db import models

# Create your models here.
class User_Data(models.Model):
    user_id = models.CharField(max_length=50)
    name = models.CharField(max_length=100, default='')
    email = models.CharField(max_length=50)
    image_url = models.CharField(max_length=100)
    likes = models.TextField()

    def __str__(self):
        return self.name + ':\n' + self.likes