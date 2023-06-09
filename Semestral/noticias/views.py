from django.db.models import Max
from django.shortcuts import render
from .models import Noticia,Foto

# Create your views here.
def Index(request):
    noticia = Noticia.objects.all()
    foto = (Foto.objects
            .values('id_noticia')
            .annotate(
							dir=Max('nom_foto')
						))
    context={
        'noticia':noticia
        ,'foto': foto
    }
    return render(request, 'Index.html',context)