from django.db import models

# Create your models here.
#item_mstr:
#1. id (Primary Key)
#2. item_name
#3. item_code
#4. price
#5. datetime
#6. status

class Item(models.Model):
    id = models.AutoField(primary_key=True)
    item_name = models.CharField(max_length=100)
    item_code = models.CharField(max_length=20)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    datetime = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=20)
  
class Supplier(models.Model):
    supplier_name = models.CharField(max_length=100)
    mobile_no = models.CharField(max_length=20)
    address = models.CharField(max_length=200)
    date = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=20)

   
    
class Purchase(models.Model):
    invoice_no = models.CharField(max_length=100)
    invoice_date = models.DateField()
    supplier = models.ForeignKey(Supplier, on_delete=models.CASCADE)
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)
    datetime = models.DateTimeField(auto_now_add=True)
    status = models.BooleanField(default=True)

    def __str__(self):
        return self.invoice_no

class PurchaseDetails(models.Model):
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    purchase_master = models.ForeignKey(Purchase, on_delete=models.CASCADE)
    datetime = models.DateTimeField(auto_now_add=True)
    status = models.BooleanField(default=True)

class Sale(models.Model):
    customer_name = models.CharField(max_length=100)
    mob_number = models.CharField(max_length=20)
    invoice_no = models.CharField(max_length=100)
    invoice_date = models.DateField()
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)
    datetime = models.DateTimeField(auto_now_add=True)
    status = models.BooleanField(default=True)

    def __str__(self):
        return self.invoice_no

class SaleDetails(models.Model):
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    qty = models.IntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    sale_master = models.ForeignKey(Sale, on_delete=models.CASCADE)
    datetime = models.DateTimeField(auto_now_add=True)
    status = models.BooleanField(default=True)  

    
  