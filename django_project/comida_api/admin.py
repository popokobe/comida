from django.contrib import admin
from .models import User, Friend, Post

myModels = [
    User,
    Friend,
    Post
]
admin.site.register(myModels)
