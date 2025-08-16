from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from trails.models import Trail
from users.models import User
from django.contrib.auth.models import Group
from .forms import UserRegisterForm, UserLoginForm,UserProfileForm,UserUpdateForm
from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect
def register(request):
    if request.method == 'POST':
     user_form = UserRegisterForm(request.POST)
     profile_form = UserProfileForm(request.POST)
     if user_form.is_valid() and profile_form.is_valid() :
      #   profile = profile_form.save(commit=False)
        user = user_form.save(commit=False)
        name = user_form.cleaned_data.get('first_name')
      #   user.profile = profile
        user_group = Group.objects.get(name='Member')
        user.save()
        user.groups.add(user_group)
        messages.success(request, f'Account created for {name}!')
        return redirect('login')
    else:
       user_form = UserRegisterForm()
       profile_form = UserProfileForm()
    return render(request, 'users/register.html', {'user_form': user_form, 'user_profile_form':profile_form})


@login_required
def profile_user(request,username):
   user=User.objects.get(username=username)
   context=Trail.objects.filter(coordinator_id=user.id).values()
   return render(request, 'users/profile.html',{'trails':context,'user':user})

@login_required 
def profile(request):
   context=Trail.objects.filter(coordinator_id=request.user.id).values()
   return render(request, 'users/profile.html',{'trails':context})

@login_required 
def update_profile(request):
   if request.method == 'POST':
      user_form = UserUpdateForm(request.POST, instance=request.user)
      profile_form = UserProfileForm(request.POST, 
                request.FILES, 
                instance=request.user.profile)
      
      if profile_form.is_valid() and user_form.is_valid():
        profile_form.save()
        user_form.save()
        messages.success(request, f'ACCOUNT UPDATED!') 
        return redirect('profile') 
   else:
    user_form=UserUpdateForm(instance=request.user)
    profile_form = UserProfileForm(instance=request.user.profile)
   return render(request, 'users/update_profile.html', {'user_profile_form':profile_form,'user_form':user_form})