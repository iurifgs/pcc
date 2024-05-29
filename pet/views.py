from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from pet.forms import AnimalForm
from .models import Animal
from django.contrib.auth.decorators import login_required
from django.urls import reverse

@login_required
def create(request):
    if request.method == 'POST':
        form = AnimalForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('index'))
    else:
        form = AnimalForm()
    return render(request, 'pet/formCreate.html', {'form': form})

@login_required
def readall(request):
    animais = Animal.objects.all()
    return render(request, "pet/index.html", {'animais': animais})

@login_required
def read(request, id_animal):
    animal = get_object_or_404(Animal, pk=id_animal)
    return render(request, "pet/detail.html", {'animal': animal})

@login_required
def update(request, id_animal):
    animal = get_object_or_404(Animal, pk=id_animal)
    if request.method == 'POST':
        form = AnimalForm(request.POST, instance=animal)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('index'))
    else:
        form = AnimalForm(instance=animal)
    return render(request, 'pet/formupdate.html', {'form': form, 'id_animal': id_animal})

@login_required
def delete(request, id_animal):
    if request.method == 'POST':
        animal = get_object_or_404(Animal, pk=id_animal)
        animal.delete()
        return HttpResponseRedirect(reverse('index'))
    else:
        # Se a solicitação não for POST, não faz nada
        return HttpResponseRedirect(reverse('index'))

@login_required
def confirmdelete(request, id_animal):
    animal = get_object_or_404(Animal, pk=id_animal)
    return render(request, 'pet/confirmdelete.html', {'animal': animal})
