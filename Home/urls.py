from django.contrib import admin
from django.urls import path
from Home import views

urlpatterns = [
   path("", views.index, name='Home'),
   path("about", views.about, name='about'),
   path("services", views.services, name='services'),
   path("contact", views.contact, name='contact'),
   path("cake", views.cake, name='cake'),
   path("pastries", views.pastries, name='pastries'),
   path("doll", views.doll, name='doll'),
   path("order", views.order, name='order'),
   path("pineapple", views.pineapple, name='pineapple'),
   path("chocolate", views.chocolate, name='chocolate'),
   path("strawberry", views.strawberry, name='strawberry'),
   path("vanila", views.vanila, name='vanila'),
   path("blueberry", views.blueberry, name='blueberry'),
   path("butterscotch", views.butterscotch, name='butterscotch')
    
]
