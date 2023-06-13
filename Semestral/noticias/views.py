from django.db.models import Max,Min
from django.shortcuts import render
from .models import Noticia,Foto
from django.contrib.auth.decorators import login_required 

# Create your views here.
def NotiFoto():
    noticia = Noticia.objects.all()
    foto = (Foto.objects
            .values('id_noticia')
            .annotate(
							dir=Max('nom_foto')
						))
    return {
        'noticia':noticia
        ,'foto': foto}


def Index(request):
    context = NotiFoto()
    return render(request, 'Index.html',context)
def Gale(request):
    context = NotiFoto()
    return render(request, 'Galeria.html',context)
def Noti(request):
    return render(request, 'Noticia.html')