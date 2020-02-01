from rest_framework import serializers
from .models import User, Friend, Post

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            'id',
            'username',
            'email',
            'password'
        )

class FriendSerializer(serializers.ModelSerializer):
    class Meta:
        model = Friend
        fields = (
            'owner',
            'friend'
        )

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = (
            'id',
            'author',
            'created_at',
            'updated_at',
            'name',
            'area',
            'address',
            'dish',
            'category',
            'expense',
            'note',
            'img',
            'rating'
        )