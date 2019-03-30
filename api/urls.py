from django.urls import path
from .views import UserCreateAPIView
from django.conf import settings
from .views import (ItemListView,ItemDetailView,UserCreateAPIView,
	UserDetailView,CartListView,CartDetailView,CartCreateView)


from rest_framework_jwt.views import obtain_jwt_token

urlpatterns = [
    path('login/', obtain_jwt_token, name='login'),
    path('register/', UserCreateAPIView.as_view(), name='register'),
    path('user/<int:user_id>/', UserDetailView.as_view(), name='api-itemlist'),
    path('itemlist/', ItemListView.as_view(), name='api-itemlist'),
    path('item/<int:item_id>/', ItemDetailView.as_view(), name='api-itemdetail'),
    path('cart/user/<int:user_id>/', CartListView.as_view(), name='api-usercart'),
    path('cartitems/<int:cart_id>/', CartDetailView.as_view(), name='api-cartdetail'),
    path('cart/create/', CartCreateView.as_view(), name='api-createcart'),
    path('login/',obtain_jwt_token,name="login"),
]


