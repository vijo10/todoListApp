from django.urls import path
from . views import Home,Update,Delete,Register,Login,Logout,Create

urlpatterns = [
    path("home",Home.as_view(),name="home"),
    path('create',Create.as_view(),name='create'),
    path("update/<int:id>",Update.as_view(),name="update"),
    path("delete/<int:id>",Delete.as_view(),name="delete"),
    path("register",Register.as_view(),name="register"),
    path("",Login.as_view(),name="login"),
    path("logout",Logout.as_view(),name="logout"),
]