from . import views
from django.urls import path

urlpatterns = [
    path('menu-items', views.MenuItemView.as_view()),
    path('menu-items/<int:pk>', views.SingleItemView.as_view()),
    path('groups/manager/users', views.UserManagerView.as_view()),
    path('groups/manager/users/<int:pk>', views.SingleUserManagerView.as_view()),
    path('groups/delivery-crew/users', views.DeliveryCrewView.as_view()),
    path('groups/delivery-crew/users/<int:pk>', views.SinlgeDeliveryCrewView.as_view()),
    path('cart/menu-items', views.CustomerCartView.as_view()),
    path('orders', views.OrderView.as_view()),
    path('orders/<int:pk>', views.SinlgeOrderView.as_view()),
]
