from django.shortcuts import redirect, render

from .forms import ClienteForm, PaisForm
from .models import Cliente, Pais


def index(request):
    return render(request, 'clientes/index.html')


def pais_list(request):
    q = request.GET.get('q')
    if q:
        query = Pais.objects.filter(nombre__icontains=q)
    else:
        query = Pais.objects.all()
    context = {'object_list': query}
    return render(request, 'clientes/pais_list.html', context)


def pais_create(request):
    if request.method == 'GET':
        form = PaisForm()

    if request.method == 'POST':
        form = PaisForm(request.POST)
        if form.is_valid():
            # print(form.cleaned_data)
            form.save()
            return redirect('clientes:pais_list')

    return render(request, 'clientes/pais_form.html', {'form': form})


def pais_detail(request, pk: int):
    query = Pais.objects.get(id=pk)
    context = {'object': query}
    return render(request, 'clientes/pais_detail.html', context)


def cliente_list(request):
    q = request.GET.get('q')
    if q:
        query = Cliente.objects.filter(nombre__icontains=q)
    else:
        query = Cliente.objects.all()
    context = {'object_list': query}
    return render(request, 'clientes/cliente_list.html', context)


def cliente_create(request):
    if request.method == 'GET':
        form = ClienteForm()

    if request.method == 'POST':
        form = ClienteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('clientes:cliente_list')

    return render(request, 'clientes/cliente_form.html', {'form': form})
