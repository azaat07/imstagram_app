from platform import release

from django.db import models

from django.contrib.auth.models import AbstractUser



class UserProfile(AbstractUser):
    bio = models.TextField()
    image = models.ImageField(upload_to='profile_image/')
    website = models.URLField()

class Follow(models.Model):
    follower = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='follower')
    following = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='following')
    created_at = models.DateTimeField(auto_now_add=True)

class Post(models.Model):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='post_owner')
    image = models.ImageField(upload_to='post_image/', null=True, blank=True)
    video = models.FileField(upload_to='post_video/', null=True, blank=True)
    description = models.TextField()
    hashtag = models.CharField(max_length=52, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

class PostLike(models.Model):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='postlike_owner')
    post = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='parent_post')
    likes = models.ManyToManyField(UserProfile, blank=True, related_name='likes_postlike')
    created_at = models.DateTimeField(auto_now_add=True)


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='comment_owner')
    text = models.TextField()
   # parent =
    created_at = models.DateTimeField(auto_now_add=True)

class CommentLike(models.Model):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='commentLike_owner')
    comment = models.ForeignKey(Comment, on_delete=models.CASCADE, related_name='commentLike')
    likes = models.ManyToManyField(UserProfile, blank=True, related_name='likes_commentlike')
    created_at = models.DateTimeField(auto_now_add=True)

class Story(models.Model):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='story_image/')
    video = models.FileField()
    created_at = models.DateTimeField(auto_now_add=True)


class Save(models.Model):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)


class SaveItem(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    save = models.ForeignKey(Save, on_delete=models.CASCADE)
    created_date = models.DateTimeField(auto_now_add=True)
