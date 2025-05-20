from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views.generic import CreateView

from member.forms import SignupForm


class SignupView(CreateView):
    model = User
    template_name = 'signup.html'
    form_class = SignupForm

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user =self.request.user
        self.object.save()

        return HttpResponseRedirect(reverse('signup'))

