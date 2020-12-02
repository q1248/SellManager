from django.urls import path

from speed import views

urlpatterns = [
    path('', views.index, name="index"),
    # path('user/', views.login, "user"),
    path('register/', views.register, name='register'),
    path('login/', views.login, name="login")

]
