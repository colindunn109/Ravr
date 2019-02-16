from django.db import models
import datetime
from django.contrib.auth import get_user_model
User = get_user_model()

from django.urls import reverse

class Post(models.Model):
    author = models.ForeignKey(User, on_delete="CASCADE")
    title = models.CharField(max_length = 128,blank=False)
    content = models.TextField(default = "")
    created_at = models.DateTimeField(auto_now = True)
    rating = models.IntegerField(default=1)
    link = models.URLField(blank=True)
    '''
    Maybe also add genre for a discover page
    so we can sort by multiple criteria for users to find what they want
    eg. Festival, New Music, etc...
    '''

    def __str__(self):
        return self.title
    '''
        Image upload to make the posts look fun
        Comments on the post
        likes on the post
        ability to share / repost the post
    '''

    def get_absolute_url(self):
        return reverse('posts:postlist')

    class Meta:
        ordering = ['-created_at']


class Comment(models.Model):
    author = models.ForeignKey(User, on_delete="CASCADE")
    post = models.ForeignKey(Post, on_delete="CASCADE")
    content = models.TextField(default="")
    rating = models.IntegerField(default=1)

    def __str__(self):
        return self.post.title

    def get_absolute_url(self):
        return reverse('posts:postlist') # TODO: make this redirect to detail page of the comment
