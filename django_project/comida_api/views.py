from django.shortcuts import render
from rest_framework import viewsets
from .models import User, Friend, Post
from .serializers import UserSerializer, FriendSerializer, PostSerializer

class UserView(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class FriendView(viewsets.ModelViewSet):
    queryset = Friend.objects.all()
    serializer_class = FriendSerializer

class PostView(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer