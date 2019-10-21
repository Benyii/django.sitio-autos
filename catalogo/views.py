from django.shortcuts import render,redirect
from .models import Auto
from .forms import AutoForm


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
    if request.method == 'POST':
        form = AutoForm((request.POST,request.FILES) or None)
        if form.is_valid():
            form.save()
            return redirect('blog')
    else:
        form = AutoForm()
    return render(request,'addpost.html',{"form":form})

	
def blog(request):

    return render(
        request,
        'blog.html',
    )
	
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
	
	
	