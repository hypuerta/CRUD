from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings

admin.autodiscover()

urlpatterns = patterns('',
	url(r'^',include('crud.apps.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$','index_view',name='vista_Principal'),
    url(r'^del_asignatura/(?P<id_asignatura>.*)', 'del_asignatura_view'),
    url(r'^del_logro/(?P<id_logro>.*)', 'del_logro_view'),
    url(r'^addasignatura/$','add_asignatura_view',name='vista_nueva_asignatura'),
    url(r'^addlogro/$','add_logro_view',name='vista_nuevo_logro'),
    url(r'^media/(?P<path>.*)$','django.views.static.serve',{'document_root':settings.MEDIA_ROOT,}),
)
