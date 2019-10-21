from django.urls import path
from . import views

urlpatterns=[
	path('inicio',views.index,name='index'),
	path('blog',views.blog,name='blog'),
	path('sobre-nosotros',views.about,name='about'),
	path('contacto',views.contact,name='contact'),
	path('addpost/',views.crearPost,name='addpost'),
]