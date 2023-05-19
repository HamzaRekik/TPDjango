from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from .forms import  UserCreationForm
from django.contrib.auth import login, authenticate
from django.contrib import messages

@login_required
def main(request):
    return render(request,'main.html')

def register(request):
    if request.method == 'POST' :
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request,user)
            messages.success(request, f'Coucou {username}, Votre compte a été créé avec succès !')
        return redirect('main')
    else :
        form = UserCreationForm()
    return render(request,'register.html',{'form' : form})