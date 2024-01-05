from django.db import models

# Create your models here.
class BlogPost(models.Model):
    title = models.CharField(max_length=256)
    content = models.TextField()
    slug = models.SlugField(max_length=256, unique=True)
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title