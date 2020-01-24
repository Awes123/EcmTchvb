from django.db import models

# Create your models here.
class Account_detail(models.Model):
    account_id=models.AutoField(primary_key=True)
    contact_person = models.CharField(max_length=50,default="")
    email=models.CharField(max_length=100,default="")
    mobile=models.CharField(max_length=20,default="")
    Houseno=models.CharField(max_length=200,default="")
    city=models.CharField(max_length=50,default="")
    Colony=models.CharField(max_length=200,default="")
    def __str__(self):
        return self.contact_person

class Account_User_ID(models.Model):
    accre_id=models.AutoField(primary_key=True)
    account_id=models.IntegerField()
    user_id=models.IntegerField()
    role=models.CharField(max_length=20,default="")