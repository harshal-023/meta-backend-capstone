from django.urls import path
from .views import sayHello, index, Bookingview, MenuItemsView, SingleMenuItemView
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('hello/', sayHello, name='sayHello'),
    path('index/', index, name='index'),
    path('booking/', Bookingview.as_view(), name='booking'),
    path('menu/', MenuItemsView.as_view(), name='menu'),
    path('menu/<int:pk>/', SingleMenuItemView.as_view(), name='single_menu_item'),
    path('api-token-auth/', obtain_auth_token),
]