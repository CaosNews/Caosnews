from django.shortcuts import render
from .models import Noticia

# Create your views here.
def Index(request):
    noticia= Noticia.objects.all()
    context={
        'noticia':noticia
    }
    return render(request, 'Index.html',context)