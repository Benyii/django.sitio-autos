from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.urls import include

urlpatterns=[
	path('inicio',views.index,name='index'),
	path('sobre-nosotros',views.about,name='about'),
	path('contacto',views.contact,name='contact'),
	path('addpost/',views.crearPost,name='addpost'),
	path('blog',views.blog,name='blog'),
	path('editpost/<int:num>/',views.actualizarPost,name='editpost'),
	path('deletepost/<int:num>/',views.borrarPost,name='deletepost'),
	path('post/<int:num>/',views.verMas,name='post'),
	path('accounts/',include('django.contrib.auth.urls'),name='accounts'),
	path('accounts/salir', views.logout, name='cuenta_salir')
]

if settings.DEBUG:
	urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)