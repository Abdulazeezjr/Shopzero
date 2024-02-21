from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views
urlpatterns = [
    path('home/', views.HomeView.as_view(),name='home'),
    path('products/',views.ItemsView.as_view(),name='product_list'),
    path('add_product/', views.ProductCreateView.as_view(),name='add_product'),
    path('product/<int:pk>/',views.ProductDetailView.as_view(),name='product_detail'),
    path('delete/<int:pk>/',views.ProductDeleteView.as_view(),name='product_delete'),
    path('update/<int:pk>/',views.ProductUpdateView.as_view(),name='product_update'),
    path('cart/', views.CartView.as_view(),name='cart_view'),
    path('addToCart/<int:product_id>/',views.AddToCartView.as_view(),name='add_to_cart'),
    path('deletefromcart/<int:pk>/',views.DeleteItemFromCartView.as_view(),name='del_from_cart'),
    path('deletefromwishlist/<int:pk>/',views.DeleteItemFromWishListView.as_view(),name='del_from_wishlist'),
    path('wishlist/', views.WishListView.as_view(),name='wishlist_view'),
    path('addToWishList/<int:pk>/',views.AddToWishListView.as_view(),name='add_to_wishlist'),
    path('categories/', views.CategoryView.as_view(),name='categories'),
    path('category_product/<int:pk>/', views.CategoryProductView.as_view(), name='cat_prod'),
    path('addreview/<int:product_id>/', views.AddReviewView.as_view(), name='add_review'),
    path('results/',views.SearchView.as_view(), name='search_results'),
    path('signup/',views.SignUp.as_view(),name='signup'),
    path('passwordChange/', views.CustomPasswordChangeView.as_view(template_name='registration/password_change_form.html'), name='password_change'),
    path('thanks/',views.ThanksView.as_view(), name='thanks'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
