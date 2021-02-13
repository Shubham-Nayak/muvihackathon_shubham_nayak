from django.urls import path
from . import views

urlpatterns=[
    path('',views.index),
    path('login/',views.login),
    path('signup/',views.signup),
    path('logout/',views.logout),
    path('checkout/<int:myid>/',views.checkout),
    path('buysubscription/',views.buysubscription),
    path('post/<int:myid>/',views.post),
    path('search/',views.search),


]