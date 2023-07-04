from django.urls import path
from .views import *
from .views import SignUpView

urlpatterns = [
    path('', Index,name='Index'),
    path('galeria/', Gale, name='Galeria'),
    path('noticia/<int:id>',Noti,name='Noticia'),
		path("signup/", SignUpView.as_view(), name="signup"),
]
