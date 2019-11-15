from django.shortcuts import render, redirect
from django.http import Http404
from .models import Auto
from .forms import AutoForm, AutoEditForm
from django.template import RequestContext
import datetime


# Create your views here.
def index(request):
    """
    Función vista para la página inicio del sitio.
    """
    # Genera contadores de algunos de los objetos principales
    #num_books=Book.objects.all().count()
    #num_instances=BookInstance.objects.all().count()
    # Libros disponibles (status = 'a')
    #num_instances_available=BookInstance.objects.filter(status__exact='a').count()
    #num_authors=Author.objects.count()  # El 'all()' esta implícito por defecto.
    
    # Renderiza la plantilla HTML index.html con los datos en la variable contexto
    return render(
        request,
        'index.html',
        #context={'num_books':num_books,'num_instances':num_instances,'num_instances_available':num_instances_available,'num_authors':num_authors},
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
    return render(request, 'post.html', {'auto': a})

def blog(request):
    autos = Auto.objects.all()
    return render(request,'blog.html', {'autos': autos})
	
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

	
	
	