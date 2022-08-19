from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=30)
    text = models.CharField(max_length=300)
    author = models.CharField(max_length=30)
    created_date = models.DateField()
    #modified_date
    #published_date
    pass

