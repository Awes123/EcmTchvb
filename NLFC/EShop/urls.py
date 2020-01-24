from django.urls import path, include
from . import  views
urlpatterns = [
    path('', views.index, name="ShopName"),
    path('about/', views.about, name="AboutUs"),
    path('contact/', views.contact, name="ContactUs"),
    path('tracker/', views.tracker, name="TrackingStatus"),
    path('Newsletters/', views.Newsletters, name="Newsletters"),
    path('returncategory/', views.returncategory, name="returncategory"),
    path('search/', views.search, name="Search"),
    path('productview/<int:myid>', views.prodView, name="Product"),
    path('checkout/', views.checkout, name="Checkout"),
    path('handlerequest/', views.handlerequest, name="Handlerequest"),
]