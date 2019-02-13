from django.shortcuts import render
from django.urls import reverse_lazy
from . import forms
from django.views.generic import CreateView, TemplateView

class SignUp(CreateView):
    form_class = forms.UserSignupForm
    success_url = reverse_lazy('login')
    template_name = 'accounts/signup.html'
