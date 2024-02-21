from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=250)

    def __str__(self) -> str:
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=250)
    price = models.DecimalField(max_digits= 10,decimal_places=2)
    quantity = models.IntegerField()
    description = models.TextField()
    release_date = models.DateField(auto_now=True)
    image = models.ImageField(upload_to='product_images/')
    category = models.ForeignKey(Category,on_delete=models.CASCADE,null=True)
    
    def __str__(self):
        return self.name
    
    def get_absolute_url(self,*args,**kwargs):
        return reverse('product_detail', kwargs={'pk': self.pk})

class CartItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveBigIntegerField(default=1)
    is_ordered = models.BooleanField(default=False)
    date_added = models.DateTimeField(auto_now=True)
    total_price = models.DecimalField(max_digits=10, decimal_places=2)

    def save(self, *args, **kwargs):
        self.total_price = self.quantity * self.product.price
        super().save(*args, **kwargs)


class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    items = models.ManyToManyField(CartItem, default=None, blank=True)

    def __str__(self):
        return f"{self.user.username}'s Cart"
    
class WishListItem(models.Model):
    wishlistitem_id = models.AutoField(primary_key=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    date_added = models.DateTimeField(auto_now=True)

class WishList(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    items = models.ManyToManyField(WishListItem, default=None, blank=True)

class Review(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product,related_name='reviews', on_delete=models.CASCADE)
    comment = models.TextField()
    rating = models.PositiveIntegerField(default=1)
    date_added = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.comment
    
    def get_absolute_url(self,*args,**kwargs):
        return reverse('product_detail', kwargs={'pk': self.product.pk})

