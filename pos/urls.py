from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('billing/', views.billing, name='billing'),
    path('billing/order', views.order, name='order'),
    #path('billpage/<int:customer_id>/', views.billpage, name='billpage'),
    path('addit/<int:product_id>/',views.addit, name="addit")
]
