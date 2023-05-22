from django.db import models
from django.contrib.auth.models import AbstractUser
from datetime import date, datetime
from api.models import Palet


class CustomUser(AbstractUser):
    photo = models.ImageField(upload_to=("users/"),blank=True,null=True)



class Category(models.Model):
    name = models.CharField(max_length=150,null=True,blank=True)

    def __str__(self):
        return self.name



class Quality(models.Model):
    cat = models.ForeignKey(Category,on_delete=models.CASCADE,blank=True,null=True)
    photo = models.ImageField(upload_to="images/quality/",null=True,blank=True)
    name = models.CharField(max_length=150,)

    def __str__(self):
        return self.name

CHOISE = (
    ("HOME",'home'),
    ("HOTEL",'hotel')
)


class Design(models.Model):
    name = models.CharField(max_length=150)
    palet = models.ForeignKey(Palet,on_delete=models.CASCADE,null=True,blank=True)
    photo = models.ImageField(upload_to="images/locations/",blank=True,null=True)
    def __str__(self):
        return self.name +" " + self.palet.name


class Product(models.Model):
    quality = models.ForeignKey(Quality,on_delete=models.CASCADE)
    color = models.CharField(max_length=150)
    design = models.ForeignKey(Design,on_delete=models.CASCADE,related_name="marks",null=True,blank=True)
    date = models.DateField(default=date.today())
    type = models.CharField(choices=CHOISE,max_length=150,blank=True,null=True)
    best = models.BooleanField(default=False)
    fire_index = models.BooleanField(default=False)
    photo = models.ImageField(upload_to="carpets/")
    sale = models.CharField(max_length=150,null=True,blank=True)
    price = models.CharField(max_length=150,blank=True)

    def __str__(self):
        return f"{self.quality} {self.color}"
    
    @property
    def Days_till(self):
        today = date.today()
        days_till = today-self.date
        new = str(days_till).split(",",1)[0]
        news = []
        num = ['d','a',' ','y',"s"]
        for i in new:
            if i not in num:
                news.append(i)
        s = ''.join(str(x) for x in news)
        if s == "0:00:00":
            return 0
        else:
            return float(s)
    @property
    def saleValue(self):
        sale = ((100 -int(self.sale)) * int(self.price))/100
        return int(sale)


class OurCustomers(models.Model):
    ip = models.CharField(max_length=150)
    other_data = models.JSONField()
    time = models.DateTimeField(default=datetime.now())

    def __str__(self):
        return self.ip

class ClientOrder(models.Model):
    user = models.ForeignKey(CustomUser,on_delete=models.CASCADE,null=True,blank=True)   
    product = models.ForeignKey(Product,on_delete=models.CASCADE,blank=True,null=True)
    comment = models.TextField()
    phone = models.CharField(max_length=150,blank=True,null=True)
    email = models.EmailField(null=True,blank=True)
    quantity = models.CharField(max_length=150,blank=True,null=True)

    def __str__(self):
        return f"{self.product} {self.phone} {self.quantity}m2"
    @property
    def Value(self):
        q = int(self.quantity)
        a = int(self.product.price)
        return q*a

class Views(models.Model):
    prod = models.ForeignKey(Product,on_delete=models.CASCADE)
    client = models.ForeignKey(OurCustomers,on_delete=models.CASCADE)

    def __str__(self):
        return self.client.ip


class Interyer(models.Model):
    CHOISES = (
    ("HOME",'home'),
    ("HOTEL",'hotel'),
    ("MAIN",'main')
    )
    type = models.CharField(max_length=150,choices=CHOISES)
    quality = models.ForeignKey(Quality,on_delete=models.CASCADE)
    photo = models.ImageField(upload_to="interyer")
    def __str__(self):
        return f"{self.quality}"