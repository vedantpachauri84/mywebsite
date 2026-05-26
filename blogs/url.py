from django.urls import path
from .import views
urlpatterns = [
    path('',views.register,name='register'),
    path('login/',views.login,name='login'),
    path('logout/',views.logout,name='logout'),
    path('index', views.index, name='index'),
    path('home/',views.allposts,name='home'),
    path('allposts',views.home,name='allposts'),
    path('allposts/<slug:blogname>/',views.about ,name='about'),


]