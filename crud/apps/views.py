from django.shortcuts import render_to_response
from django.template import RequestContext 
from django.http import HttpResponseRedirect
from crud.apps.forms import addAsignaturaForm
from crud.apps.models import Logro,Asignatura

def index_view(request):
	lista_asinatura = Asignatura.objects.filter(activo=True)
	lista_logro = Logro.objects.filter(activo=True)
	return render_to_response('index.html', locals(),context_instance=RequestContext(request))

def add_asignatura_view(request):
	if request.method == 'POST':
		nombre = request.POST['nombre']
		pesoAsignatura = request.POST['peso']
		activo = True
		asignatura = Asignatura(nombre=nombre,pesoAsignatura=pesoAsignatura,activo=activo)
		asignatura.save()
		return HttpResponseRedirect('/')
	else:
		return render_to_response('addasignatura.html',context_instance=RequestContext(request))


def add_logro_view(request):
	if request.method == 'POST':
		asignatura = request.POST['asignatura']
		idAsignatura = Asignatura.objects.get(nombre=asignatura)
		nombre = request.POST['nombre']
		descripcion = request.POST['descripcion']
		activo=True
		logro = Logro(idAsignatura=idAsignatura,nombre=nombre,descripcion=descripcion,activo=activo)
		logro.save()
		return HttpResponseRedirect('/')
	else:
		asignaturas = Asignatura.objects.all()
		return render_to_response('addlogro.html',locals(),context_instance=RequestContext(request))

