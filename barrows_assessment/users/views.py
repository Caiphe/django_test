from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserRegistrationForm, UserUpdateForm, ProfileUpdateForm
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse


# This fucntion create new users and redirect them to the signin page where they can login using the  Authentication cridentials
def SignUp(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(
                request, f" Account Created for {username}. Please sign in ! ")
            return redirect('sign-in')
    else:
        form = UserRegistrationForm()
    return render(request, 'users/signup.html', {'form': form})


# The bellow function updates the profile user's profile details .
@login_required
def profile(request):
    if request.method == 'POST' :
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(
            request.POST, request.FILES,  instance=request.user.profile)

        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(
                request, f"Your account has been updated !!!")
            # return JsonResponse({"success": True}, status=200)
            return redirect('profile')
        # return JsonResponse({"success": False}, status=400)

    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)

    context = {
        'u_form': u_form,
        'p_form': p_form
    }
    return render(request, 'users/profile.html', context)
