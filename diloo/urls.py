from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()


from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'diloo.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^sobre/$','diloo_mtv.views.sobre'),
    url(r'^preguntas/$', 'diloo_mtv.views.pregunta'),
   

    url(r'^ajaxexample/$', 'diloo_mtv.views.main'),
  
    url(r'^post$', 'diloo_mtv.views.post'),
    url(r'^monitoreo$', 'diloo_mtv.views.monitoreo'),
  	url(r'^push$', 'diloo_mtv.views.push'),
    url(r'^ori$', 'diloo_mtv.views.ori'),
    url(r'^orillamadas/$', 'diloo_mtv.views.orillamadas'),

)

urlpatterns += staticfiles_urlpatterns()