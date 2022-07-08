from django.db import models

# Create your models here.

class Product(models.Model):
    pId = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    price = models.FloatField()
    brandName = models.TextField()
    currentStock = models.IntegerField()
    image = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.name

class Offers(models.Model):
    oId = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    code = models.TextField()
    percentOff = models.IntegerField()
    dateCreated = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name


class Customers(models.Model):
    cId = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    email = models.EmailField()
    phone = models.IntegerField()
    token = models.IntegerField()
    isVerified = models.BooleanField(default=False)
    dateCreated = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name


class Slot(models.Model):
    sId = models.AutoField(primary_key=True)
    
    # time field with 1 hour interval 
    slotTime = models.DateTimeField()
    slotRemaining = models.IntegerField(default=5)
    # time field with 1 hour interval 



    def __str__(self):
        date = self.slotTime
        date = str(date)
        return date

class Service(models.Model):
    sId = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    price = models.FloatField()

    def __str__(self):
        return self.name

class Booking(models.Model):
    bId = models.AutoField(primary_key=True)
    customer = models.ForeignKey(Customers, on_delete=models.CASCADE, null=True)
    slot = models.ForeignKey(Slot, on_delete=models.CASCADE, null=True)
    service = models.ForeignKey(Service, on_delete=models.CASCADE, null=True)
    dateCreated = models.DateField(auto_now_add=True)
