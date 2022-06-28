from django.shortcuts import render

# Create your views here.
from django.views.generic import TemplateView


class ChatTemplate(TemplateView):
    template_name = 'chat.html'


