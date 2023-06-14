from django.urls import path
from .views import *

urlpatterns = [
    path('', Index,name='Index'),
    path('galeria/', Gale, name='Galeria'),
    path('noticia/<int:id>',Noti,name='Noticia'),
]
