from django.urls import path
from owner import views

urlpatterns=[
    path("index",views.DashBoardView.as_view(),name="dashboard"),
    path("orders/latest",views.OrderView.as_view(),name="new-orders"),
    path("orders/details/<int:id>",views.OrderDetailView.as_view(),name="order-details")
]