from django.urls import path
from .views import *

urlpatterns = [
    path('', Index,name='Index'),
    path('galeria/', Gale, name='Galeria'),
    path('noticia/<int:id>',Noti,name='Noticia'),
		path('post/',Noticia_View.as_view(),name='Publicar'),
		path("signup/", SignUpView.as_view(), name="signup"),
]
