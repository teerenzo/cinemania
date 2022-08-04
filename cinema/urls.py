from django.urls import path
from django.contrib.auth import views
from . import views as regural

urlpatterns=[
path("",regural.home,name='index'),
path('login/', views.LoginView.as_view(), name='login'),
path('logout/', views.LogoutView.as_view(), name='logout'),
path('signup/', regural.signup_view, name="signup"),
path('addMovie/', regural.addMovie, name="addmovie"),
path('viewMovie/<str:id>', regural.singleMovie, name="viewMovie")

]