from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    STATUS =(
        ('S', 'Satis qiymet'),
        ('E', "Endirim qiymeti")
    )
    locations = models.TextField()
    phone = models.CharField(max_length=50)
    status = models.CharField(max_length=50, choices=STATUS)
    
    def __str__(self):
        return self.phone


class Banner(models.Model):
    name = models.CharField(max_length=50)
    content = models.TextField()
    image = models.ImageField(upload_to='banner_imgs/')
    
    class Meta:
        ordering = ("-id",)
    
    def __str__(self):
        return self.name
    
    
class Category(models.Model):
    name = models.CharField(max_length=50)
    image = models.ImageField(upload_to='category_imgs/')
    
    class Meta:
        ordering = ("-id",)
    
    def __str__(self):
        return self.name
    
    
class Marka(models.Model):
    name = models.CharField(max_length=50)
    
    class Meta:
        ordering = ("-id",)
    
    def __str__(self):
        return self.name
    
    
class Product(models.Model):
    name = models.CharField(max_length=50)
    image = models.ImageField(upload_to='product_imgs/')
    image_1 = models.ImageField(upload_to='product_imgs/')
    price = models.FloatField(default=0)
    percentage = models.FloatField(default=0)
    discount_price = models.FloatField(default=0)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='products')
    marka = models.ForeignKey(Marka, on_delete=models.CASCADE, related_name='products')
    
    class Meta:
        ordering = ("-id",)
        
    def __str__(self):
        return self.name
    

    
class Advantages(models.Model):
    name = models.CharField(max_length=50)
    content = models.TextField()
    icon = models.CharField(max_length=40)
    
    class Meta:
        ordering = ("-id",)
        verbose_name_plural = "Advantages"
    
    def __str__(self):
        return self.name
    
    
class Look(models.Model):
    name = models.CharField(max_length=50)
    value_name = models.CharField(max_length=60)
    
    class Meta:
        ordering = ("-id",)
    
    def __str__(self):
        return self.name
    
    
class Service(models.Model):
    content = models.TextField()
    image = models.ImageField(upload_to='service_imgs/')
    
    class Meta:
        ordering = ("-id",)
    
    def __str__(self):
        return self.content
    
    
class Mission(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    image = models.ImageField(upload_to='mission_imgs/')
    
    class Meta:
        ordering = ("-id",)
    
    def __str__(self):
        return self.title
    
    
class Form(models.Model):
    name = models.CharField(max_length=50)
    surname = models.CharField(max_length=50)
    email = models.EmailField(max_length=256)
    phone = models.CharField(max_length=20)
    note =  models.TextField()
    
    class Meta:
        ordering = ("-id",)
    
    def __str__(self):
        return self.name
    
    
class Media(models.Model):
    link = models.URLField(max_length=256)
    icon = models.CharField(max_length=50)
    
    class Meta:
        ordering = ("-id",)
    
    def __str__(self):
        return self.link
    

class SiteSettings(models.Model):
    logo = models.CharField(max_length=50, blank=True, null=True)
    performans_image = models.ImageField(upload_to='settings_imgs/', blank=True, null=True)
    performans_content = models.TextField(blank=True, null=True)
    performans_name = models.CharField(max_length=100, blank=True, null=True)
    corparative_name = models.CharField(max_length=50, blank=True, null=True)
    corparative_content = models.TextField(blank=True, null=True)
    corparative_image = models.ImageField(upload_to='settings_imgs/', blank=True, null=True)
    login = models.CharField(max_length=60, blank=True, null=True)
    location = models.TextField(blank=True, null=True)
    
    
    class Meta:
        verbose_name = "Settings"
        verbose_name_plural = "Settings"
        
    def save(self, *args, **kwargs):
        if not self.id and SiteSettings.objects.exists():
            return None
        return super(SiteSettings,self).save(*args,**kwargs)
        

    def __str__(self):
        return "Settings"
    
    

class Basket(models.Model):
    user =models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name="baskets")
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="product_baskets")
    quantity = models.IntegerField(default=0)
    
    class Meta:
        ordering = ("-id",)
    
    
    def __str__(self):
        return self.name
    
    
    
class Order(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="product_orders")
    user =models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name="orders")
    quantity = models.IntegerField(default=0)
    
    class Meta:
        ordering = ("-id",)
  
    
    def __str__(self):
        return self.basket.name + " " + self.product.name