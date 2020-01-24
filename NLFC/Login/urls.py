from django.urls import path, include
from . import  views
urlpatterns = [
    path('', views.login, name="login"),
    path('login/', views.login, name="login"),
    path('logout/', views.logout, name="logout"),
    path('verifyemail/', views.verifyemail, name="verifyemai"),
    path('register/', views.register, name="register"),
    path('reset/', views.reset_password, name="reset"),
]