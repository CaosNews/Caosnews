from django.db import models

# Create your models here.
class Tipo_Parti(models.Model):
	id_tp_part = models.AutoField(db_column='IdTipo_Part',primary_key=True)
	tipo_part = models.CharField(max_length=20)
	def __str__(self):
		return str(self.tipo_part)

class Categoria(models.Model):
	id_categoria = models.AutoField(db_column='IdCategory',primary_key=True)
	nom_category = models.CharField(max_length=25, blank=False, null=False)
	def __str__(self):
		return str(self.nom_category)

class Parti(models.Model):
	id_parti = models.IntegerField(primary_key=True,db_column='Id_Parti')
	Nombre = models.CharField(max_length=30)
	Apellido = models.CharField(max_length=30)
	Rut = models.IntegerField()
	dv = models.CharField(max_length=1)
	correo = models.EmailField(unique=True, max_length=100, blank=True, null=True)
	fono = models.IntegerField()
	id_tp_part = models.ForeignKey(Tipo_Parti,on_delete=models.CASCADE,db_column='IdTipo_Part')
	def __str__(self):
		return str(self.Nombre)+' '+str(self.Apellido)

class Noticia(models.Model):
	id_noticia = models.IntegerField(primary_key=True,db_column='Id_Noticia')
	fecha = models.DateTimeField(blank=False,null=False)
	titulo = models.CharField(max_length=35)
	Detalle = models.CharField(max_length=120)
	Ubicacion = models.CharField(max_length=120)
	id_categoria = models.ForeignKey(Categoria,on_delete=models.CASCADE,db_column='IdCategory')
	id_parti = models.ForeignKey(Parti,on_delete=models.CASCADE,db_column='Id_Parti')
	def __str__(self):
		return str(self.titulo)

class Form_contact(models.Model):
	id_form_cont = models.IntegerField(primary_key=True,db_column='Id_form_cont')
	nombre = models.CharField(max_length=30)
	apellido = models.CharField(max_length=30)
	correo = models.EmailField(unique=True, max_length=100, blank=True, null=True)
	fono = models.IntegerField()
	decripcion = models.CharField(max_length=120)
	titulo = models.CharField(max_length=35)
	def __str__(self):
		return str(self.titulo)+' |'+str(self.nombre)+' '+str(self.apellido)