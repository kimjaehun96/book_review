from django.db import models
from django.utils import timezone
# from django.utils

# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=50)
    content = models.TextField()
    created_date = models.DateTimeField( default= timezone.now)
    price = models.IntegerField(null=True)
    score = ((1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5'))
    rating=models.IntegerField(
        
        choices=score, 
        default=1,
    
    )
    img = models.FileField(null = True)
    def __str__(self):
        return self.title
        
class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete = models.CASCADE, related_name='comments') #댓글이 속한 글이 지워지면 댓글들도 다 지우도록 함.
    content = models.TextField()
    