from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import HttpResponseRedirect
from crud.apps.models import Logro,Asignatura  

def index_view(request):
	lista_asinatura = Asignatura.objects.filter(activo=True)

	return render_to_response('index.html', locals(),context_instance=RequestContext(request))




def productos_view(request,pagina):
	lista_prod = Producto.objects.filter(status=True)
	paginator = Paginator(lista_prod,3)
	try:
		page = int(pagina) # por seguridad convierte la pagina enviada a int
	except:
		page = 1 # si no es un entero, la pagina por default es 1
	try:
		productos = paginator.page(page) # trae los productos q tiene page
	except(EmptyPage,InvalidPage):
		productos = paginator.page(paginator,num_pages)#envia a la ultima pagina
	ctx = {'productos':productos}
	return render_to_response('home/productos.html',ctx,context_instance=RequestContext(request))