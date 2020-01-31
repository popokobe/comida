from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

class User(models.Model):
    username = models.CharField(max_length=20)
    email = models.EmailField()
    password = models.CharField(max_length=20)

class Friend(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='owner')
    friend = models.ForeignKey(User, on_delete=models.CASCADE, related_name='friend')

class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    name = models.CharField(max_length=50)
    area = models.CharField(max_length=50)
    address = models.CharField(max_length=50, blank=True)
    dish = models.CharField(max_length=100, blank=True)
    category = models.CharField(max_length=20)
    expense = models.IntegerField(blank=True)
    note = models.TextField(blank=True)
    img = models.ImageField(
        blank=True,
        upload_to='post_image'
    )
    rating = models.IntegerField(
        validators=[
            MinValueValidator(1),
            MaxValueValidator(5)
        ]
    )

    def __str__(self):
        return self.name