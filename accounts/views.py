from django.shortcuts import render,redirect
from .forms import UserRegistrationForm,UserUpdateForm
from django.urls import reverse_lazy
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login,logout

def signup(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            user = form.save()
            login(request, user)
            print(user)
            return redirect(reverse_lazy('profile'))
    else:
        form = UserRegistrationForm()
    
    return render(request, 'signup.html', {'form': form})
def login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect(reverse_lazy('homepage'))
    else:
        form = AuthenticationForm()
    
    return render(request, 'login.html', {'form': form})

def user_logout_view(request):
    if request.user.is_authenticated:
        logout(request)
    return redirect(reverse_lazy('homepage'))

def profile(request):
    if request.method == 'POST':
        form = UserUpdateForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('profile')  # Redirect to the user's profile page
    else:
        form = UserUpdateForm(instance=request.user)
    
    return render(request,'profile.html', {'form': form})