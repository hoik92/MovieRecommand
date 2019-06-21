from django.shortcuts import render, redirect, get_object_or_404
from .forms import CustomUserCreationForm, CustomUserChangeForm
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

# Create your views here.

def signup(request):
    # POST: 유저 등록
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)
            return redirect('movies:list')
        return redirect('accounts:signup')
    # GET: 유저 정보 입력
    else:
        form = CustomUserCreationForm()
        return render(request, 'accounts/signup.html', {'form': form})
        
def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            auth_login(request, form.get_user())
            # next= 정의되어 있으면 
            return redirect(request.GET.get('next') or 'movies:list')
        return redirect('accounts:user_login')
    else:
        form = AuthenticationForm()
        return render(request, 'accounts/login.html', {'form': form})
        


def user_logout(request):
    auth_logout(request)
    return redirect('movies:list')
    
@login_required
def user_admin(request):
    if request.user.is_superuser:
        users = User.objects.all()
        return render(request, 'accounts/admin.html', {'users': users})
    else:
        return redirect('movies:list')
        
@login_required
def user_detail(request, user_id):
    if request.user.is_superuser:
        user = get_object_or_404(User, id=user_id)
        if request.method == 'POST':
            form = CustomUserChangeForm(request.POST, instance=user)
            if form.is_valid():
                form.save()
                return redirect('accounts:admin')
        else:
            form = CustomUserChangeForm(instance=user)
            return render(request, 'accounts/detail.html', {'form': form, 'euser': user})
    else:
        return redirect('accounts:admin')
        
@login_required
def user_delete(request, user_id):
    if request.user.is_superuser:
        user = get_object_or_404(User, id=user_id)
        user.delete()
        return redirect('accounts:admin')