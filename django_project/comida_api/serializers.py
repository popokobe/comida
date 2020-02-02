from rest_framework import serializers
from .models import User, Friend, Post

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = (
            'id',
            'url',
            'username',
            'email',
            'password'
        )

class FriendSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Friend
        fields = (
            'owner',
            'friend'
        )

class PostSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Post
        fields = (
            'id',
            'url',
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