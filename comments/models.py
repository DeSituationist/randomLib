from django.db import models
from ..books.models import BookInfo

# Create your models here.
class Comment(models.Model):
    nickname = models.CharField(max_length=50)
    email = models.EmailField()
    text = models.TextField(max_length=200)
    published_at = models.DateTimeField(auto_now_add=True)
    book = models.ForeignKey(BookInfo, on_delete=models.CASCADE, related_name='comments')
    visible = models.BooleanField(default=True)

    class Meta:
        ordering = ['-published_at']
        indexes = [models.Index(fields=['-published_at'])]

    def __str__(self): return f'{self.nickname}: {self.text[:30]}'