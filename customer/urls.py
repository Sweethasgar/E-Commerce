from django.contrib import admin
from django.urls import path, include
from customer import views

urlpatterns = [
    path("register", views.RegisterView.as_view(), name="register"),
    path("login", views.LoginView.as_view(), name="login"),
    path("home", views.HomeView.as_view(), name="home"),
    path("products/<int:id>", views.ProductDetailView.as_view(), name="product-detail"),
    path("products/<int:id>/cart/add", views.AddCartView.as_view(), name="add-to-cart"),
    path("cart/all", views.MyCartView.as_view(), name="my-cart"),
    path("cart/my cart/<int:cid>/<int:pid>", views.CheckOutView.as_view(), name="check-out"),
    path("cart/remove/<int:id>", views.cartitem_remove, name="remove"),
    path("logout", views.logout_view, name="logout")
]
