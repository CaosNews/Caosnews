# TO-DO

- un formulario para noticias de la gente
- diseño de la pagina noticias
- inicio de sesion? para los periodistas
- ~~modelo de BD~~
- paginas y diseño
- ~~que noticia.destacada sea Boolean~~
- ~~que se puedan linkear varias fotos en la noticia~~
- ~~Id de noticia y participante automatica~~

---

## Instrucciones para instalar

- activa el dev-env con

		> cd Dev-nev/Scripts
		> Activate
		> cd../..
	en el cmd prompt(terminal)
- Instala Django y el cliente de MySql con

		> pip install -r ../reqs.txt
		> pip install mysqlclient
	Una vez hecho esto el proyacto funcionara normalmente

- hacer las migraciones con

		> py manage.py makemigrations
		> py manage.py migrate
	Asegurate de que el MySQL comunnity server este instalado y conectado en
	```python
	settings.py
	```