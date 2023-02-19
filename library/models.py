from django.db import models

# Create your models here.
# class Userdb(models.Model):
#     Uname = models.CharField(max_length=100, null=True, blank=True)
#     Email = models.EmailField()
#     Password = models.CharField(max_length=100)
#     Cpassword = models.CharField(max_length=100)
class Userdbook(models.Model):
     Uname = models.CharField(max_length=100, null=True, blank=True)
     Email = models.EmailField(null=True,blank=True)
     Password = models.CharField(max_length=100,null=True,blank=True)
     Cpassword = models.CharField(max_length=100,null=True,blank=True)

class Contactdb(models.Model):
     Username = models.CharField(max_length=100, null=True, blank=True)
     Emailid = models.EmailField(null=True, blank=True)
     Message = models.CharField(max_length=500, null=True, blank=True)

