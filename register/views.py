# views.py em register
from django.shortcuts import render, redirect
from .forms import CustomUserCreationForm

def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')  # Redirecionar para a página index
    else:
        form = CustomUserCreationForm()
    return render(request, 'registration/cadastro.html', {'form': form})

# views.py em pet
from django.shortcuts import render

def index(request):
    return render(request, 'index/pet/index.html')

def login_view(request):
    return render(request, 'register/login.html')