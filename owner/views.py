from django.shortcuts import render, redirect
from owner.models import *
# Create your views here.
from django.views.generic import TemplateView, ListView, DetailView
from owner.models import Orders
from owner.forms import OrderUpdateForm
from django.core.mail import send_mail


class DashBoardView(TemplateView):
    template_name = "dashboard.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        cmt = Orders.objects.filter(status="order-placed").count()
        context["count"] = cmt
        return context


class OrderView(ListView):
    model = Orders
    context_object_name = "orders"
    template_name = "admin-orderlist.html"

    def get_queryset(self):
        return Orders.objects.filter(status="order-placed")


class OrderDetailView(DetailView):
    model = Orders
    template_name = "order-detailview.html"
    pk_url_kwarg = "id"
    context_object_name = "order"

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        form = OrderUpdateForm
        context["form"] = form
        return context

    def post(self, request, *args, **kwargs):
        order = self.get_object()
        print(self.get_object())
        form = OrderUpdateForm(request.POST)
        if form.is_valid():
            order.status = form.cleaned_data.get("status")
            order.expected_delivery_date = form.cleaned_data.get("expected_delivery_date")
            dt = form.cleaned_data.get("expected_delivery_date")
            order.save()
            send_mail(
                "order delivery updated future store",
                f"your order will be deliverd on(dt)",
                "sweethasgar2@gmail.com",
                ["sweethasgar3@gmail.com"]

            )
            print(form.cleaned_data)
            return redirect("home")
