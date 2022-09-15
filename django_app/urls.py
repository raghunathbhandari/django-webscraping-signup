from django.contrib import admin
from django.urls import path
from django_app import views

urlpatterns = [
   path("", views.home, name="home"),
   path("about", views.about, name="about"),
   path("register", views.registration, name="registration"),
   path("login", views.userlogin, name="login"),
   path("contact", views.contact, name="contact"),
   path("logout", views.userlogout, name="logout"),
    path("verifyuser/", views.verifyuser, name="verifyuser"),
    path("sendlink", views.sendlink, name="sendlink"),
    path("movielist", views.webscraping, name="movielist"),

   # path('activate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/',  activate, name='activate'),  

   #verifyuser?key=fbb28dca-33f6-11ed-a032-39a54afdf081
   #http://127.0.0.1:8000/verifyuser/fbb28dca-33f6-11ed-a032-39a54afdf081

]

