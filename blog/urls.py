from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('add/', views.addBlog),
    path('blog/<str:id>/', views.blogDetail),
    path('edit/<str:id>/', views.editBlog),
    path('delete/<str:id>/', views.deleteBlog),
    path('login/', views.loginUser),
    path('register/', views.registerUser),
    path('logout/', views.logoutUser),
]