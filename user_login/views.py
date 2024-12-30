from django.shortcuts import render,redirect
from . import forms
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.forms import AuthenticationForm,PasswordChangeForm,SetPasswordForm
# Create your views here.
def signup(request):
    if request.method == 'POST':
        form =  forms.user_signup(request.POST)
        if form.is_valid():
            messages.success(request,'Account Creation Successful')
            form.save()
            return redirect('login')
    else:
        form = forms.user_signup()
    return render(request,'signup.html',{'form':form})

def user_login(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            form = AuthenticationForm(request = request, data = request.POST)
            if form.is_valid():
                name = form.cleaned_data['username']
                user_pass = form.cleaned_data['password']
                user = authenticate(username = name, password = user_pass)
                if user is not None:
                    login(request,user)
                    return redirect('profile')
        else:
            form = AuthenticationForm()
        return render(request,'login.html',{'form':form})
    else:
        return redirect('profile')
