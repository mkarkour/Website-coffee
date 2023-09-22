from django.urls import path
from . import views

urlpatterns = [
    path('accueil', views.Welcome),
    #path('article/<id_article>', views.view_article),
]