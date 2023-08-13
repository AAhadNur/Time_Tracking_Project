
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.contrib import messages

from userprofile.models import Userprofile
from team.models import Team

# Create your views here.


@login_required
def myaccount(request):
    teams = request.user.teams.exclude(
        pk=request.user.userprofile.active_team_id)

    context = {'teams': teams}

    return render(request, 'userprofile/myaccount.html', context)


@login_required
def edit_profile(request):
    if request.method == 'POST':
        request.user.first_name = request.POST.get('first_name', '')
        request.user.last_name = request.POST.get('last_name', '')
        request.user.email = request.POST.get('email', '')
        request.user.save()

        messages.info(request, 'The changes of your account was saved')

        return redirect('myaccount')

    return render(request, 'userprofile/edit_profile.html')


def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)

        if form.is_valid():
            user = form.save()
            user.email = user.username
            user.save()

            userprofile = Userprofile.objects.create(user=user)

            login(request, user)

            return redirect('home')
    else:
        form = UserCreationForm()

    context = {
        'form': form,
    }

    return render(request, 'userprofile/signup.html', context)
