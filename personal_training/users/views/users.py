# Django
from django.views.generic import FormView
from django.urls import reverse_lazy
from django.contrib.auth import login

# Forms
from personal_training.users.forms import SignUpForm


class SignUpView(FormView):
    template_name = 'users/register.html'
    form_class = SignUpForm

    success_url = reverse_lazy('users:pending')

    def form_valid(self, form):
        user = form.save()
        # Force login
        login(self.request, user)
        return super().form_valid(form)
