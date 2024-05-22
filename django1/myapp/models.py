from django.db import models

# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=100)
    body = models.TextField()

    def __str__(self) -> str:
        return self.title
    
    def snippet(self):
        return self.body[:30]

            

