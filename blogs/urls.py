from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

app_name = 'blogs'

urlpatterns = [
    path('', views.index, name='index'),
    path('new/', views.new_post, name='new_post'),
    path('edit/<int:post_id>/', views.edit_post, name='edit_post'),
    path('login/', auth_views.LoginView.as_view(template_name='blogs/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='blogs/logout.html'), name='logout'),
    path('register/', views.register, name='register'),
]
