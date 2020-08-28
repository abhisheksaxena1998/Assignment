from django.db import models

# Create your models here.
class UserFeedBack(models.Model):
    userid = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100)
    description = models.TextField()
    reply = models.TextField()
    replied = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)



class Url(models.Model):
    index = models.AutoField(primary_key=True)
    text = models.CharField(max_length=1000,null=True,default="Not Found")
    name = models.CharField(max_length=1000,null=True,default="Not Found")
    result = models.CharField(max_length=100,null=True,default="Not Found")
    time = models.CharField(max_length=1000,null=True,default="Not Found")
    pno = models.CharField(max_length=100,null=True,default="Not Found")
    uid = models.CharField(max_length=100,null=True,default="Not Found")
    #bookedat = models.DateTimeField(auto_now_add=True)
    created_at = models.DateTimeField(auto_now_add=True)

