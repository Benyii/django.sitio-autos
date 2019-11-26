from django.shortcuts import render, redirect
from django.http import Http404
from .models import Auto, Comentario
from .forms import AutoForm, AutoEditForm, ComentarioForm
from django.template import RequestContext
import datetime


# Create your views here.
def index(request):
    num_visits=request.session.get('num_visits', 0)   
    num_visits=request.session['num_visits']=num_visits+1 
    # Renderiza la plantilla HTML index.html con los datos en la variable contexto
    return render(
        request,
        'index.html',
        context={'num_visits':num_visits},
    )

def crearPost(request):
    if 'submit_button' in request.POST:
        formulario = AutoForm(request.POST, request.FILES)
        if formulario.is_valid(): 
            formulario.save()
            return redirect('blog')
    else:
        formulario = AutoForm()
    return render(request,'addpost.html',{"form":formulario})

def actualizarPost(request, num):
    context_instance=RequestContext(request)
    auto_list = Auto.objects.all()
    #auto = Auto.objects.get(id=id)
    #formulario = AutoForm(request.POST or None, instance=auto)
    if request.method == 'POST':
        a = Auto.objects.get(pk=int(num))
        formulario = AutoEditForm(request.POST, instance=a)

        if formulario.is_valid():
            formulario.save()
            return redirect('blog')
    else:
        a = Auto.objects.get(pk=int(num))
        formulario = AutoEditForm(instance=a)
    
    return render(request, 'editpost.html', {'form': formulario}, {'auto': a})

def borrarPost(request, num):
    a = Auto.objects.get(pk=int(num))

    if request.method == 'POST':
        a.delete()
        return redirect('blog')
    
    return render(request, 'deletepost-confirm.html', {'auto': a})

def verMas(request, num):
    a = Auto.objects.get(pk=int(num))
    comentarios = Comentario.objects.all()
    formulario = ComentarioForm(request.POST)

    if request.method == 'POST':
        if formulario.is_valid(): 
            formulario.save()
    else:
        formulario = ComentarioForm()
        
    return render(request, 'post.html', {'auto': a}, {'form': formulario})

def blog(request):
    autos = Auto.objects.all()
    cantidad = Auto.objects.count()
    return render(request,'blog.html', {'autos': autos}, {'cantidad': cantidad})
	
def about(request):

    return render(
        request,
        'about.html',
    )	

def contact(request):

    return render(
        request,
        'contact.html',
    )	

def logout(request):

    return render(
        request,
        'registration/logout.html',
    )

	
	
	