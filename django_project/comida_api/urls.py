from django.urls import path, include
from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register('users', views.UserView)
router.register('friends', views.FriendView)
router.register('posts', views.PostView)


urlpatterns = [
    path('', include(router.urls))
]