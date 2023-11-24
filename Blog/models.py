import  datetime
from django.db import models

# Create your models here.
# class Postimage(models.Model):
    

#     def __str__(self):
#         return f"name = {self.name}, picture = {self.resturant_img}"

class Profile(models.Model):
    #user  
    username = models.CharField(max_length=50, unique=True)
    firstname = models.CharField(max_length=70)
    email = models.EmailField()
    password =  models.CharField(max_length=100)
    profile_img =  models.ImageField(upload_to= 'images/', default = 'images/images.png')

    # basic
    website = models.URLField(blank=True )
    location = models.CharField(max_length=120,  blank=True )
    bio = models.TextField(max_length = 300, blank=True )
    tag = models.TextField(max_length = 300, blank=True )
    
    # coding
    learning = models.TextField(max_length = 300, blank=True ) #currently learnig what
    available = models.TextField( max_length = 300, blank=True ) #discussion you  are available for 
    skill = models.TextField(max_length = 300, blank=True )
    project = models.TextField(max_length = 300, blank=True ) #current project

    # work
    work = models.CharField(max_length=200, blank=True )
    education = models.CharField(max_length=200, blank=True) 


    def __str__(self):
        return f"username= {self.username}, firstname= {self.firstname}, email= {self.email}, password= {self.password}"
    
class Post(models.Model):
    post_img = models.ImageField(upload_to='images/', blank = True)
    title = models.CharField(max_length=100)
    authour = models.CharField(max_length=50 )
    content = models.TextField(max_length=10000)
    hashtag = models.CharField(max_length=10000, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    
    
    def __str__(self):
        return f"Title= {self.title}, Authour= {self.authour}, Content= {self.content}, Image= {self.post_img}, Created on-{self.created}"
    

