from django.db import models

class Tweet(models.Model):
    # id = models.AutoField(primary_key=True)
    content = models.TextField(blank=True, null=True) # blank=not required in Django, null=Not req in DB
    image = models.FileField(upload_to='image/', blank=True, null=True)

