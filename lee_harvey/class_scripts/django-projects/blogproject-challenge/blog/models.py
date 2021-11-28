from django.db import models


# Create your models here.
class Tag(models.Model):
    tag_id = models.AutoField(primary_key = True)
    name = models.CharField(max_length = 255)
    
    def __str__(self):
        return self.name

class Post(models.Model):
    post_id = models.AutoField(primary_key = True)
    img_link = models.URLField()
    title =  models.CharField(max_length = 255)
    body = models.TextField()
    tags = models.ManyToManyField(Tag)
    
    def __str__(self):
        return self.title
    
    @property
    def comments(self):
        responses = Comment.objects.all().order_by('-id')
        return Comment.objects.filter(Post, responses)

class Comment(models.Model):
    comment_id = models.AutoField(primary_key = True)
    comment = models.TextField()
    post = models.ForeignKey(Post, default = 1, on_delete = models.CASCADE)
    
    def __str__(self):
        return self.comment