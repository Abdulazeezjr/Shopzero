from django.contrib import admin
from .models import Product,Category, Cart, CartItem, WishList, WishListItem, Review

# Register your models here.
admin.site.register(Product)
admin.site.register(Category)
admin.site.register(CartItem)
admin.site.register(Cart)
admin.site.register(WishListItem)
admin.site.register(WishList)
admin.site.register(Review)