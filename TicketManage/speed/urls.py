from django.urls import path

from speed import views

urlpatterns = [
    path('', views.index, name="index"),
    path('news/<str:PK>', views.news, name="news"),
    path('register/', views.register, name='register'),
    path('login/', views.login, name="login"),
    path('space', views.space, name="space"),
    path('logout/', views.logout, name="logout"),
    path('myprofile/', views.myprofile, name="myprofile"),
    path('welcome/', views.index, name="welcome"),
    path('welcome/buy/<str:PK>/', views.buy, name="buy"),
    path('welcome/remove/<str:PK>/', views.remove, name="remove"),
    path('privage/', views.privage, name="privage"),
]
