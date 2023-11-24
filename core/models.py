from django.db import models

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=200, blank=True)
    content = models.TextField(max_length=100000, blank=True)
    def __str__( self):
        return f"title = {self.title}, content = {self.content}"

