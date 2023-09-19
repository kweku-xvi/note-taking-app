from django.shortcuts import render, redirect
from .forms import RegisterAccount, UserInfo, ProfileImage
from django.contrib.auth.decorators import login_required
from django.contrib import messages

def register(response):
    if response.method == 'POST':
        form = RegisterAccount(response.POST)

        if form.is_valid():
            username = form.cleaned_data['username']
            messages.success(response, f'Account created for {username}!')
            form.save()
            return redirect('login')
    else:
        form = RegisterAccount()
    return render(response, 'register/register.html', {'form':form})

@login_required
def profile(request):
    if request.method == 'POST':
        user_form = UserInfo(request.POST, instance=request.user)
        profile_form = ProfileImage(request.POST, request.FILES, instance=request.user.profile)

        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()

            return redirect('/profile')
    else:
        user_form = UserInfo(instance=request.user)
        profile_form = ProfileImage(instance=request.user.profile)
    return render(request, 'register/profile.html', {'u_form':user_form, 'p_form':profile_form})