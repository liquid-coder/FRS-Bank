from django.shortcuts import render,redirect
from .forms import UserRegistrationForm,UserUpdateForm
from django.urls import reverse_lazy
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login,logout
from django.contrib.auth.decorators import user_passes_test
from django.contrib.auth.models import User
from transactions.models import LoanRequest

def signup(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            return redirect('login')
    else:
        form = UserRegistrationForm()
    
    return render(request, 'signup.html', {'form': form})
def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        is_admin = request.POST.get('is_admin') == 'on'
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                if is_admin and user.is_staff:
                    return redirect('admin_dashboard')
                else:
                    return redirect('homepage')
    else:
        form = AuthenticationForm()
    
    return render(request, 'login.html', {'form': form})

def user_logout(request): 
    if request.user.is_authenticated:
        logout(request)
    return redirect('homepage')

def profile(request):
    if request.method == 'POST':
        form = UserUpdateForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('profile')  # Redirect to the user's profile page
    else:
        form = UserUpdateForm(instance=request.user)
    
    return render(request,'profile.html', {'form': form})

@user_passes_test(lambda u: u.is_staff)
def admin_dashboard(request):
    users = User.objects.all()
    loan_requests = LoanRequest.objects.all()
    return render(request, 'admin_dashboard.html', {'users': users, 'loan_requests': loan_requests})

@user_passes_test(lambda u: u.is_staff)
def delete_user(request, user_id):
    user = User.objects.get(id=user_id)
    user.delete()
    return redirect('admin_dashboard')

@user_passes_test(lambda u: u.is_staff)
def approve_loan(request, loan_id):
    loan = LoanRequest.objects.get(id=loan_id)
    loan.status = 'approved'
    loan.save()
    return redirect('admin_dashboard')

@user_passes_test(lambda u: u.is_staff)
def disapprove_loan(request, loan_id):
    loan = LoanRequest.objects.get(id=loan_id)
    loan.status = 'disapproved'
    loan.save()
    return redirect('admin_dashboard')