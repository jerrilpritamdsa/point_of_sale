from django.urls import path
from pos import views

urlpatterns = [
    path('pos/', views.dashboard, name='dashboard'),
    path('billing/', views.billing, name='billing'),
    #path('cusomer/', views.cusomer, name='cusomer'),
    path('billing/order', views.order, name='order'),
    #path('billing/subtract_add/<int:product_id>/', views.subtract_add, name='subtract_add'),
    #path('billpage/<int:customer_id>/', views.billpage, name='billpage'),
    #path('addit/<int:product_id>/',views.addit, name="addit")
]
