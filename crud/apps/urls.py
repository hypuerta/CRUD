from django.conf.urls.defaults import patterns,url

urlpatterns = patterns('crud.apps.views',
    url(r'^$','index_view',name='vista_index'),
    url(r'^add/asignatura/$','add_asignatura_view',name='vista_nueva_asignatura'),
    url(r'^add/logro/$','add_logro_view',name='vista_nuevo_logro'),
)