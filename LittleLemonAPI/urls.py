from . import views
from django.urls import path

urlpatterns = [
    path('menu-items/', views.MenuItemView.as_view(), name='menu-items'),
    path('menu-items/<int:pk>/', views.SingleItemView.as_view(), name='single-item'),
    path('groups/manager/users/', views.UserManagerView.as_view(), name='manager-users'),
    path('groups/manager/users/<int:pk>/', views.SingleUserManagerView.as_view(), name='single-manager-user'),
    path('groups/delivery-crew/users/', views.DeliveryCrewView.as_view(), name='delivery-crew'),
    path('groups/delivery-crew/users/<int:pk>/', views.SinlgeDeliveryCrewView.as_view()),
    path('cart/menu-items/', views.CustomerCartView.as_view(), name='customer-cart'),
    path('orders/', views.OrderView.as_view(), name='orders'),
    path('orders/<int:pk>/', views.SinlgeOrderView.as_view(), name='single-order'),
]
