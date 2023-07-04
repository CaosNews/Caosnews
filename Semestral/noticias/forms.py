from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms

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