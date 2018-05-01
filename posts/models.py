from django.db import models
from django.utils import timezone
from tinymce.models import HTMLField

class Post(models.Model):
    """
    A single Blog Post
    """
    title = models.CharField(max_length=200)
    content = HTMLField()
    created_date = models.DateTimeField(auto_now_add=True)
    published_date = models.DateTimeField(blank=True, null=True,
                                          default=timezone.now)
    views = models.IntegerField(default=0)
    tag = models.CharField(max_length=30, blank=True, null=True)
    image = models.ImageField(upload_to="img", blank=True, null=True)

    def __str__(self):
        return self.title