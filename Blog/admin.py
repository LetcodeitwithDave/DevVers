from django.contrib  import admin

from .models import Profile, Post

class PostAdmin(admin.ModelAdmin):
    list_display = ["title", "content", "hashtag", "authour", "created", "post_img"]
    
class UserAdmin(admin.ModelAdmin):
    list_display = ["username", "firstname", "email", "password", "profile_img"]

# Register your models here.
admin.site.register(Profile, UserAdmin)
admin.site.register(Post, PostAdmin)

 