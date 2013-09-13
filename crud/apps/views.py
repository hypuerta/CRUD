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

def del_asignatura_view(request, id_asignatura):
	try:
		asignatura = Asignatura.objects.get(idAsignatura = id_asignatura)
		asignatura.delete()
	except Asignatura.DoesNotExist:
		return HttpResponseRedirect("/")
	
	return HttpResponseRedirect("/")

def del_logro_view(request, id_logro):
	try:
		logro = Logro.objects.get(idLogro = id_logro)
		logro.delete()
	except Logro.DoesNotExist:
		return HttpResponseRedirect("/")
	
	return HttpResponseRedirect("/")

def edit_logro_view(request,id_logro):
	try:		
		logro = Logro.objects.get(idLogro = id_logro)
		if request.method == 'POST':
			if logro:
				asig = request.POST['asignatura']
				nombre = request.POST['nombre']
				descripcion = request.POST['descripcion']
				asignatura = Asignatura.objects.get(nombre = asig)
				logro.idAsignatura = asignatura
				logro.nombre = nombre
				logro.descripcion = descripcion
				logro.save()
				return HttpResponseRedirect('/')
		asignaturas = Asignatura.objects.filter(activo = True)
		ctx = {'logro':logro, 'asignaturas':asignaturas}
		return render_to_response('edit_logro.html',ctx,context_instance=RequestContext(request))
	except Logro.DoesNotExist:
		return HttpResponseRedirect("/")

def edit_asignatura_view(request,id_asignatura):
	try:
		asignatura = Asignatura.objects.get(idAsignatura = id_asignatura)
		if request.method == 'POST':
			form = addAsignaturaForm(request.POST,request.FILES)
			if form.is_valid():
				nombre = form.cleaned_data['nombre']
				pesoAsignatura = form.cleaned_data['pesoAsignatura']
				activo = form.cleaned_data['activo']
				asignatura.nombre = nombre
				asignatura.pesoAsignatura = pesoAsignatura
				asignatura.activo = activo
				asignatura.save()
				return HttpResponseRedirect('/')
		if request.method == 'GET':
			form = 	addAsignaturaForm(initial={
									'nombre':asignatura.nombre,
									'pesoAsignatura':asignatura.pesoAsignatura,
									'activo':asignatura.activo
				})
		ctx = {'form':form,'asignatura':asignatura}
		return render_to_response('edit_asignatura.html',ctx,context_instance=RequestContext(request))
	except Logro.DoesNotExist:
		HttpResponseRedirect("/")

