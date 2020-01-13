from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login

# Create your views here.

def signup_view(request):
    form = UserCreationForm()
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
    
    context ={
        'form': form
    }
    return render(request, 'signup.html', context)

def login_view(request):
    form = AuthenticationForm(data=request.POST)
    context = {}
    if form.is_valid():
        user= form.get_user()
        login(request, user)
        return redirect('../../details/')
    context['form'] = form
    return render(request, 'login.html', context)
