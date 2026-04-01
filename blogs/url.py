from django.urls import path
from .import views
urlpatterns = [
    path('home/',views.allposts,name='home'),
    path('allposts',views.home,name='allposts'),
    path('allposts/<slug:blogname>/',views.about ,name='about'),

]