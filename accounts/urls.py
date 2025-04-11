from django.urls import path, include
from accounts import views

urlpatterns = [
    path('login/', views.LoginView.as_view(), name='loin'),
    path('register/', views.RegisterView.as_view(), name='register')


]
