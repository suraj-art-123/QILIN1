from django.db import models

# Create your models here.
from django.db import models

class Contact(models.Model):
    sno = models.AutoField(primary_key=True)
    name=models.CharField(max_length=30)
    phon=models.CharField(max_length=13)
    email=models.CharField(max_length=100)
    content=models.TextField()
    timeStamp=models.DateTimeField(auto_now_add=True,blank=True)
    def __str__(self):
        return "Message from " + self.name
#class BlogComment(models.Model):
    