from django.shortcuts import render
from django.views.generic import DetailView, CreateView, DeleteView, TemplateView, View, ListView, FormView
from owner.models import *
from django.contrib.auth.models import User
from django.urls import reverse_lazy
from customer import forms
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.shortcuts import render, redirect


# Create your views here.

class RegisterView(CreateView):
    model = User
    template_name = "register.html"
    form_class = forms.RegistrationForm
    success_url = reverse_lazy("login")


class LoginView(View):
    def get(self, request, *args, **kwargs):
        form = forms.LoginForm()
        return render(request, "login.html", {"form": form})

    def post(self, request, *args, **kwargs):
        form = forms.LoginForm(request.POST)
        if form.is_valid():
            uname = form.cleaned_data.get("username")
            pwd = form.cleaned_data.get("password")
            user = authenticate(request, username=uname, password=pwd)
            if user:
                login(request, user)
                msg = "login successfull"
                messages.success(request, msg)

                if request.user.is_superuser:
                    msg = "login successfull"
                    messages.success(request, msg)

                    return redirect("dashboard")

                else:

                    return redirect("home")

            else:
                msg = "login failed"
                messages.error(request, msg)

                return render(request, "login.html", {"form": form})

        return render(request, "login.html")


class HomeView(TemplateView):
    template_name = "home.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["products"] = Products.objects.all()
        return context


class ProductDetailView(DetailView):
    template_name = "product-detail.html"
    pk_url_kwarg = "id"
    context_object_name = "product"
    model = Products


class AddCartView(FormView):
    template_name = "add-cart.html"
    form_class = forms.CartFrom

    def get(self, request, *args, **kwargs):
        id = kwargs.get("id")
        product = Products.objects.get(id=id)
        return render(request, self.template_name, {"form": forms.CartFrom, "product": product})

    def post(self, request, *args, **kwargs):
        id = kwargs.get("id")
        product = Products.objects.get(id=id)
        qty = request.POST.get("qty")
        user = request.user
        Carts.objects.create(product=product, qty=qty, user=user)
        return redirect("home")


class MyCartView(ListView):
    template_name = "my-cart.html"
    model = Carts
    context_object_name = "carts"

    def get_queryset(self):
        return Carts.objects.filter(user=self.request.user).exclude(status="cancelled").order_by("-created_date")


class CheckOutView(FormView):
    template_name = "check-out.html"
    form_class = forms.CheckOutForm

    def post(self, request, *args, **kwargs):
        cart_id = kwargs.get("cid")
        product_id = kwargs.get("pid")
        user = request.user
        cart = Carts.objects.get(id=cart_id)
        product = Products.objects.get(id=product_id)
        delivery_address = request.POST.get("address")
        Orders.objects.create(product=product,
                              user=user,
                              delivery_address=delivery_address
                              )
        cart.status = "order-placed"
        cart.save()
        return redirect("home")


def cartitem_remove (request, *args, **kwargs):
    id = kwargs.get("id")
    cart = Carts.objects.get(id=id)
    cart.status = "cancelled"
    cart.save()
    return redirect("my-cart")



def logout_view(request):
    logout(request)
    return redirect("login")
