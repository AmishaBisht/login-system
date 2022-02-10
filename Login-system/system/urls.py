from django.urls import path,include
from . import views

urlpatterns = [
       path("",views.Indexpage,name="index"),
       path("signin/",views.Signin,name="signin"),
       path("signout/",views.Signout,name="signout"),
       path("signup/",views.Signup,name="signup"),
]
