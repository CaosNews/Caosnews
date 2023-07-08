from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import *

class signUpForm(UserCreationForm):
	email = forms.EmailField(widget=forms.EmailInput(attrs={'class':'form-control','style':'font-size: medium;'}))
	class Meta:
		model = User
		fields = ('username', 'email', 'password1','password2')
	def __init__(self,*args,**kwargs):
		super(signUpForm,self).__init__(*args,**kwargs)
		self.fields['username'].widget.attrs['class']='form-control'
		self.fields['username'].widget.attrs['style']='font-size: medium;'

		self.fields['password1'].widget.attrs['class']='form-control'
		self.fields['password1'].widget.attrs['style']='font-size: medium;'

		self.fields['password2'].widget.attrs['class']='form-control'
		self.fields['password2'].widget.attrs['style']='font-size: medium;'
#custom field cuz y not
class DTL_input(forms.DateTimeInput):
    input_type = "datetime-local"
class DTL_field(forms.DateTimeField):
    input_formats = [
        "%Y-%m-%dT%H:%M:%S", 
        "%Y-%m-%dT%H:%M:%S.%f", 
        "%Y-%m-%dT%H:%M"
    ]
    widget = DTL_input(format="%Y-%m-%dT%H:%M")
    

class FormNoticia(forms.ModelForm):
	fecha = DTL_field()
	class Meta:
		model = Noticia
		fields = "__all__"
	def __init__(self,*args,**kwargs):
		super(FormNoticia,self).__init__(*args,**kwargs)
		for v in self.fields:
			self.fields[v].widget.attrs['class']='form-control'
			self.fields[v].widget.attrs['style']='font-size: medium;'
			if v == "destacada":
				self.fields[v].widget.attrs['class']='form-check-input'
			if v == "id_categoria" or v == "id_parti":
				self.fields[v].widget.attrs['class']='form-select'