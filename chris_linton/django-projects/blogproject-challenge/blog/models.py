from django.db import models

# Create your models here.
class Tag(models.Model):
    tag_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)

class Post(models.Model):
    post_id = models.AutoField(primary_key=True)
    img_link = models.URLField()
    title =  models.CharField(max_length=255)
    body = models.TextField()
    tags = models.ManyToManyField(Tag)

# for modeling each comment instance
class Comment(models.Model):
    # create a field that will contain a unique identifier for each comment
    comment_id = models.AutoField(primary_key=True)
    # create a field that will contain the text of the comment body
    comment = models.TextField()
    # create a field that will contain a unique identifier for each post
    post_id = models.ForeignKey(Post, on_delete=models.CASCADE)