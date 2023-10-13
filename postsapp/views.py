from django.shortcuts import render
from django.views.generic import ListView

from .models import post
# Create your views here.

class homepage(ListView):
    model = post
    template_name = 'homepage.html'
    context_object_name = 'all_messages'

