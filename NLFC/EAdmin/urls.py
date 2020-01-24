from django.urls import path, include
from .import views
urlpatterns = [
    path('', views.dashboard, name="EAdmin"),
    path('Dashboard/', views.dashboard, name="dashboard"),
    path('Product/', views.Products, name="Product"),
    path('AddProduct/', views.AddProduct, name="AddProduct"),
    path('searchcategory/', views.searchcategory, name="searchcategory"),
    path('searchproduct/', views.searchproduct, name="searchproduct"),
    path('searchunit/', views.searchunit, name="searchunit"),
   ]