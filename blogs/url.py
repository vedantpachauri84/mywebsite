from django.urls import path
from .import views
urlpatterns = [
    path('home/',views.home,name='home'),
    path('',views.allposts,name='allposts'),
    path('allposts/<slug:blogname>/',views.about ,name='about'),

]