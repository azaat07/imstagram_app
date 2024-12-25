from .views import *
from rest_framework import routers
from django.urls import path, include


router = routers.DefaultRouter()
router.register(r'user', UserProfileViewSet, basename='user_list')
router.register(r'follow', FollowViewSet, basename='follow_list')
router.register(r'post', PostViewSet, basename='post_list')
router.register(r'postlike', PostLikeViewSet, basename='postlike_list')
router.register(r'comment', CommentViewSet, basename='comment_list')
router.register(r'CommentLike', CommentLikeViewSet, basename='commentlike_list')
router.register(r'story', StoryViewSet, basename='story_list')
router.register(r'save', SaveViewSet, basename='save_list')
router.register(r'saveitem', SaveItemViewSet, basename='saveItem_list')


urlpatterns = [
    path('', include(router.urls)),
    path('register/', RegisterView.as_view(), name='register'),

]