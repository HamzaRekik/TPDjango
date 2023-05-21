from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from .forms import  UserCreationForm
from django.contrib.auth import login, authenticate
from django.contrib import messages
from django.contrib.auth.models import User

@login_required
def main(request):
    if request.user.is_authenticated:
        request.session['username'] = request.user.username
    return render(request,'main.html')

def register(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        email = request.POST.get('email')
        user = User.objects.create(username=username , password= password,email=email)
        messages.success(request, 'votre compte a été créé avec succès!')
        return redirect('main')
    
        
    return render(request, 'register.html')