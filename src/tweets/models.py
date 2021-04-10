from django.db import models
import random
from django.conf import settings

User = settings.AUTH_USER_MODEL

class Tweet(models.Model):
    # id = models.AutoField(primary_key=True)
    user = models.ForeignKey (User, on_delete=models.CASCADE) # many users can have many tweets
    content = models.TextField(blank=True, null=True) # blank=not required in Django, null=Not req in DB
    image = models.FileField(upload_to='image/', blank=True, null=True)

    #def __str__(self):
    #    return self.content

    class Meta:
        ordering = ['-id']

    def serialize(self):
        return {
            "id": self.id,
            "content": self.content,
            "likes": random.randint(0, 200)
        }

