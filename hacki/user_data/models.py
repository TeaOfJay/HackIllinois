from django.db import models

class user_data(models.Model):
    user_id = models.CharField(max_length=200)
    first_name = models.CharField(max_length=1000)
    last_name = models.CharField(max_length=1000)
    interests = models.CharField(max_length=1000)