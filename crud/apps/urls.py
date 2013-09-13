from django.conf.urls.defaults import patterns,url

urlpatterns = patterns('crud.apps.views',
    url(r'^$','index_view',name='vista_index'),
    url(r'^add/asignatura/$','add_asignatura_view',name='vista_nueva_asignatura'),
    url(r'^add/logro/$','add_logro_view',name='vista_nuevo_logro'),
    url(r'^delete/asignatura/(?P<id_asignatura>.*)/$', 'del_asignatura_view'),
    url(r'^edit/asignatura/(?P<id_asignatura>.*)/$','edit_asignatura_view',name='vista_edit_asignatura'),
    url(r'^delete/logro/(?P<id_logro>.*)/$', 'del_logro_view',name='vista_delete_logro'),
    url(r'^edit/logro/(?P<id_logro>.*)/$','edit_logro_view',name='vista_edit_logro'),
)