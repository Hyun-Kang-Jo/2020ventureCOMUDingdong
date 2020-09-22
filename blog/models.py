from django.db import models

# Create your models here.

class Blog(models.Model):
    title = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    description = models.CharField(max_length=500,default='')
    body = models.TextField()

    def __str__(self):
        return self.title

    def summary(self):
        return self.body[:100]

class Photo(models.Model):
    post = models.ForeignKey(Blog, on_delete = models.CASCADE, null=True)
    image = models.ImageField(upload_to='images/',blank=True,null=True)