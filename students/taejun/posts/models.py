import datetime

from django.db              import models
from django.db.models.query import QuerySet

class Post(models.Model):
    user        = models.ForeignKey("users.User", on_delete    = models.CASCADE, related_name = 'posts')
    desc        = models.TextField(blank=True)
    image       = models.CharField(max_length=150)
    liked_users = models.ManyToManyField("users.User", related_name="liked_posts", through='Like')
    created_at  = models.DateTimeField(auto_now_add=True)
    changed_at  = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'posts'

    def __str__(self):
        return self.desc


class CommentQuerySet(QuerySet):
    def update(self, *args, **kwargs):
        super().update(*args, is_changed=True,  **kwargs)


class Comment(models.Model):
    objects    = CommentQuerySet.as_manager()
    post       = models.ForeignKey('Post', on_delete=models.CASCADE)
    user       = models.ForeignKey('users.User', on_delete=models.CASCADE)
    content    = models.CharField(max_length=1500)
    is_changed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    changed_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'comments'

    def __str__(self):
        return self.content


class Like(models.Model):
    post = models.ForeignKey('Post', on_delete=models.CASCADE)
    user = models.ForeignKey('users.User', on_delete=models.CASCADE)

    class Meta:
        db_table = 'posts_likes'
