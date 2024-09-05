from django.urls import path
from . import views 

urlpatterns = [
    path('', views.home),
    path("showProducts/<id>",views.showProducts), 
    path("viewDetails/<id>",views.viewDetails),
    path("login",views.login),
    path("signUp",views.signUp),    
    path('logout',views.logout),
    path('addToCart',views.addToCart),
    path('showAllCartItems',views.showAllCartItems),
    path('searchbar',views.searchbar),
    path('addtocart',views.addtocart),
    path('addToWishlist',views.addToWishlist),
    path('showAllWishlist',views.showAllWishlist),
    path('makePayment',views.makePayment),
    path('showProfile',views.showProfile),
    path('address',views.address),
    path('yourOrders',views.yourOrders),

]
