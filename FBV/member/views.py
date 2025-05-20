from django.shortcuts import render, redirect
from django.template.context_processors import request
from django.urls import reverse

from member.forms import SignupForm


def Signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse('signup'))
    else:
        form = SignupForm()

    return render(request, 'signup.html', {'form': form})


