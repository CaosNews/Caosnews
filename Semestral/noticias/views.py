from django.db.models import Max
from django.shortcuts import render
from .models import Noticia, Foto
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django.views import generic
from .forms import signUpForm

# para el register y back *shrugs*

class SignUpView(generic.CreateView):
    form_class = signUpForm
    success_url = reverse_lazy("login")
    template_name = "registration/signup.html"

# Create your views here.
def S_NotiFoto(id_n):
	noticia = Noticia.objects.all().filter(pk=id_n)
	foto = Foto.objects.all().filter(id_noticia__exact=id_n)
	return {
			'noticia':noticia,
			'fotos': foto
	}
def A_NotiFoto():
	noticia = Noticia.objects.all()
	foto = Foto.objects.values("id_noticia").annotate(dir=Max("nom_foto"))
	return {
		"noticia": noticia,
		"foto": foto
	}

def Index(request):
	context = A_NotiFoto()
	return render(request, "Index.html", context)

def Gale(request):
	context =A_NotiFoto()
	return render(request, "Galeria.html", context)

def Noti(request, id):
	context = S_NotiFoto(id)
	return render(request, "Noticia.html",context)
