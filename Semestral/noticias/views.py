from django.shortcuts import render
from .models import Noticia,Foto

# Create your views here.
def Index(request):
    noticia = Noticia.objects.all()
    foto = Foto.objects.all()
    context={
        'noticia':noticia
        ,'foto': foto
    }
    return render(request, 'Index.html',context)