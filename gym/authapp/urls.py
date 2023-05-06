
from django.urls import path
from authapp import views

urlpatterns = [
   path('',views.Home,name="Home"),
   path('signup',views.signup,name="signup"),
   path('login',views.loginfunc,name="loginfunc"),
   path('logout',views.logoutfunc,name="logoutfunc"),
   path('contact',views.contact,name="contact"),
   path('join',views.join,name="join"),
   path('profile',views.profile,name="profile"),
   path('gallery',views.gallery,name="gallery"),
    path('attendance',views.attendance,name="gallery")

]
