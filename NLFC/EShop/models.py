from django.db import models

# Create your models here.

class Product(models.Model):
    product_id = models.AutoField
    product_name = models.CharField(max_length=50)
    category_id = models.IntegerField()
    subcategory = models.CharField(max_length=50,default="")
    sales=models.CharField(max_length=50,default="")
    price =  models.IntegerField()
    sprice =  models.IntegerField()
    desc = models.CharField(max_length=300)
    pub_date = models.DateField()
    Unit=models.CharField(max_length=50,default="")
    Qty=models.IntegerField(default=0)
    status=models.BooleanField(default=False)
    image=models.ImageField(upload_to="EShop/images",default="")
    image1=models.ImageField(upload_to="EShop/images",default="")
    image2=models.ImageField(upload_to="EShop/images",default="")
    def __str__(self):
        return self.product_name

class Productcategory(models.Model):
    category_id = models.AutoField(primary_key=True)
    category = models.CharField(max_length=50, default="")
    pub_date = models.DateField(auto_now=True)
    def __str__(self):
        return self.category
 

class Contact(models.Model):
    msg_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=70, default="")
    phone = models.CharField(max_length=70,default="")
    comments = models.CharField(max_length=500,default="")

    def __str__(self):
        return self.name

class Newsletter(models.Model):
    newsletter_id = models.AutoField(primary_key=True)
    Email = models.CharField(max_length=100)

class Orders(models.Model):
    order_id = models.AutoField(primary_key=True)
    items_json=models.CharField(max_length=5000)
    amount=models.IntegerField(default=0)
    name=models.CharField(max_length=100)
    email=models.CharField(max_length=111)
    address=models.CharField(max_length=200)
    city=models.CharField(max_length=50)
    state=models.CharField(max_length=50)
    zip_code=models.CharField(max_length=20)
    phone=models.CharField(max_length=20)

    def __str__(self):
        return self.name

class OrderUpdate(models.Model):
    update_id=models.AutoField(primary_key=True)
    order_id=models.IntegerField(default="")
    update_desc=models.CharField(max_length=5000)
    timestamp=models.DateField(auto_now_add=True)

    def __str__(self):
        return self.update_desc[0:7]+"...."