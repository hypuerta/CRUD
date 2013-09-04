from django.conf.urls.defaults import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('crud.apps.views',
    # Examples:
    # url(r'^$', 'crud.views.home', name='home'),
    # url(r'^crud/', include('crud.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$','index_view',name='vista_Principal'),
    url(r'^del_asignatura/(?P<id_asignatura>.*)', 'del_asignatura_view'),
    url(r'^del_logro/(?P<id_logro>.*)', 'del_logro_view'),
    url(r'^addasignatura/$','add_asignatura_view',name='vista_nueva_asignatura'),
    url(r'^addlogro/$','add_logro_view',name='vista_nuevo_logro'),
    url(r'^edit_asignatura/(?P<id_asignatura.*)','edit_asignatura_view', name = "vista_editar_asignatura"),
)
