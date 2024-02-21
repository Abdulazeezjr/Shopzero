from typing import Any
from django.db.models.query import QuerySet
from django.forms.models import BaseModelForm
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from django.views import generic
from django.contrib.auth.views import PasswordChangeView
from django.urls import reverse_lazy, reverse
from django.contrib.auth import authenticate
from django.shortcuts import redirect, get_object_or_404, HttpResponseRedirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import UserCreationForm, PasswordChangeForm
from . import models
# Create your views here

class HomeView(generic.TemplateView):
    template_name = 'shopzero/home.html'

class ProductCreateView(generic.CreateView):
    template_name = 'shopzero/products.html'
    model = models.Product
    fields = '__all__'

class ItemsView(generic.ListView):
    model = models.Product
    template_name = 'shopzero/product_list.html'

class ProductDetailView(generic.DetailView):
    model = models.Product
    template_name = 'shopzero/product_detail.html'

class ProductUpdateView(generic.UpdateView):
    model = models.Product
    fields = '__all__'
    template_name = 'shopzero/product_update.html'

class ProductDeleteView(generic.DeleteView):
    model = models.Product
    template_name = 'shopzero/product_delete.html'
    success_url = reverse_lazy('product_list')

class AddToCartView(LoginRequiredMixin,generic.View):
    def post(self, request, product_id):
        try:
            quantity = int(request.POST.get('quantity', 1))
        except ValueError:
            quantity = 1

        product = get_object_or_404(models.Product, pk=product_id)
        cart, created = models.Cart.objects.get_or_create(user=request.user)
        cart_item, created = cart.items.get_or_create(product=product)
        
        cart_item.quantity = quantity
        product.quantity -= quantity
        product.save() 
        cart_item.save()
        return redirect('cart_view')

    def get(self, request, product_id):
        return self.post(request, product_id)
    
class CartView(LoginRequiredMixin, generic.TemplateView):
    template_name = 'shopzero/cart.html'

    def get(self, request):
        cart, created = models.Cart.objects.get_or_create(user=request.user)
     
        # Calculate the total price of items in the cart
        total_price = sum(item.product.price * item.quantity for item in cart.items.all())
        # Pass the cart and total price to the template context
        context = self.get_context_data(cart=cart, total=total_price)
        return self.render_to_response(context)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Retrieve the cart object again to ensure its existence
        cart = get_object_or_404(models.Cart, user=self.request.user)
        # Pass the cart object to the template context
        context['cart'] = cart
        return context
    
class DeleteItemFromCartView(LoginRequiredMixin, generic.DeleteView):
    model = models.CartItem
    success_url = reverse_lazy('cart_view')

    def post(self, request, *args, **kwargs):
        cart_item = self.get_object()
        product = cart_item.product
        product.quantity += cart_item.quantity
        product.save()
        return super().post(request, *args, **kwargs)

class AddToWishListView(LoginRequiredMixin, generic.View):
    def get(self, request, pk):
        wish, created = models.WishList.objects.get_or_create(user=request.user)
        product = get_object_or_404(models.Product,pk=pk)
        wish_item, created = wish.items.get_or_create(product=product)
        wish_item.save()
        return redirect('wishlist_view')

class WishListView(LoginRequiredMixin, generic.TemplateView):
    template_name = 'shopzero/wishlist.html'
    def get(self,request):
        wish,created = models.WishList.objects.get_or_create(user=request.user)
        context = self.get_context_data(wish=wish)
        return self.render_to_response(context)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        wish = get_object_or_404(models.WishList, user=self.request.user)
        context['wish']  = wish
        return context

class DeleteItemFromWishListView(LoginRequiredMixin, generic.DeleteView):
    model = models.WishListItem
    success_url = reverse_lazy('wishlist_view')
    
class CategoryView(generic.ListView):
    template_name = 'shopzero/category.html'
    model = models.Category

class CategoryProductView(generic.TemplateView):
    template_name = 'shopzero/category_product.html'
    def get(self,request, pk):
        category = get_object_or_404(models.Category, pk=pk)
        context = self.get_context_data(category=category)
        return self.render_to_response(context)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        product = models.Product.objects.filter(**kwargs)
        context['products'] = product
        print(context)
        print(kwargs)
        return context

class AddReviewView(LoginRequiredMixin, generic.CreateView):
    template_name = 'shopzero/addreview.html'
    model = models.Review
    fields = ['rating', 'comment']

    def form_valid(self, form):
        product_id = self.kwargs['product_id']
        product = get_object_or_404(models.Product, pk=product_id)
        form.instance.product = product
        form.instance.user = self.request.user
        return super().form_valid(form)
    
    def get_absolute_url(self):
        return reverse_lazy('product_detail',kwargs={'pk':self.kwargs['product_id']})


class SearchView(generic.TemplateView):
    template_name = "shopzero/search_results.html"

    def get(self, request):
        query = request.GET.get('query')
        results = models.Product.objects.filter(name__icontains=query)
        return render(request, self.template_name, {'results':results})
    
class SignUp(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy("login")
    template_name = 'registration/signup.html'

class CustomPasswordChangeView(PasswordChangeView):
    form_class = PasswordChangeForm
    success_url = reverse_lazy('password_change_done')
    template_name = 'registration/password_change_form.html'


class ThanksView(generic.TemplateView):
    template_name = 'shopzero/thanks.html'