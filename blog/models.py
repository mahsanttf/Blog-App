from django.db import models
from django.contrib.auth.models import User


class BlogAuthor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    author_name = models.CharField(max_length=200)
    author_bio = models.TextField()

    def __str__(self):
        return self.author_name


class Blog(models.Model):
    author = models.ForeignKey(BlogAuthor, on_delete=models.CASCADE, related_name='blogs')
    blog_name = models.CharField(max_length=200)
    blog_desc = models.TextField()
    post_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-post_date']

    def __str__(self):
        return self.blog_name


class BlogComment(models.Model):
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE, related_name='comments')
    comment_desc = models.TextField('Description:')
    comment_date = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        ordering = ['-comment_date']

    def __str__(self):
        return self.comment_desc
