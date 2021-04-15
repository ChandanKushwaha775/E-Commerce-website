from django.db import models

# Create your Product models here.
class Product(models.Model):
    product_id = models.AutoField
    product_name = models.CharField(max_length=50)
    cotegory=models.CharField(max_length=50, default='')
    subcotegory=models.CharField(max_length=50, default='')
    price=models.IntegerField(default=0)
    desc = models.CharField(max_length=5000)
    pub_date = models.DateField()
    image=models.ImageField(upload_to="shop/images", default='')

    def __str__(self):
        return self.product_name

# Create your contact models here.
class Contact(models.Model):
    msg_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=70, default="")
    phone = models.CharField(max_length=70, default="")
    desc = models.CharField(max_length=500, default="")


    def __str__(self):
        return self.name

class Orders(models.Model):
    order_id = models.AutoField(primary_key=True)
    items_json = models.CharField(max_length=5000)
    amount=models.IntegerField(default=0)
    name = models.CharField(max_length=150)
    email = models.CharField(max_length=200)
    phone = models.CharField(max_length=111,default="")
    # landmark = models.CharField(max_length=1000)
    address = models.CharField(max_length=2000)
    state = models.CharField(max_length=111)
    city = models.CharField(max_length=111)
    zip_code = models.CharField(max_length=111)


class OrderUpdate(models.Model):
    update_id = models.AutoField(primary_key=True)
    order_id = models.IntegerField(default="")
    update_desc = models.CharField(max_length=5000)
    timestamp = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.update_desc[0:7] + "..."