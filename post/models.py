from django.db import models

# Create your models here.
class Post(models.Model):
    name = models.CharField(max_length=100,null=False,blank=False)
    author = models.CharField(max_length=100,null=False,blank=False)
    description = models.TextField(null=False,blank=False)
    created_at =models.DateField(null=False,blank=False)

    def __str__(self):

        return f'{self.name} by {self.author}'