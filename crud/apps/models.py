from django.db import models

class Asignatura(models.Model):
	idAsignatura = models.AutoField(primary_key=True,blank=False,null=False)
	nombre = models.CharField(max_length=100,null=False)
	pesoAsignatura = models.IntegerField(null=False)
	activo = models.BooleanField(default=True,null=False)
	fechaCreacion = models.DateField(auto_now_add=True,null=False)

	def __unicode__(self):
		return self.nombre

class Logro(models.Model):
	idLogro = models.AutoField(primary_key=True,blank=False,null=False)
	idAsignatura = models.ForeignKey(Asignatura)
	nombre = models.CharField(max_length=500,null=False)
	descripcion = models.TextField(max_length=2000)
	activo = models.BooleanField(default=True,null=False)
	fechaCreacion = models.DateField(auto_now_add=True,null=False)

	def __unicode__(self):
		return self.nombre
