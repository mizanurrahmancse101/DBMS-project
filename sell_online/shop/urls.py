from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name = "index"),
    path('about/', views.about, name = "Aboutus"),
    path('account/', views.account, name = "account"),
    path('shop/', views.shop, name = "shop"),
    path('contact/', views.contact, name = "Contactus"),
    path('tracker/', views.tracker, name = "TrackerStatus"),
    path('search/', views.search, name = "Search"),
    path("products/<int:myid>", views.productView, name="ProductView"),
    path('checkout/', views.checkout, name = "Checkout"),
    path('register/', views.register, name="register"),
	path('login/', views.login, name="login"),  
	path('logout/', views.logoutUser, name="logout"),

]
