from django.shortcuts import render
from django.http import HttpResponse
from django.views import generic


class HomePageView(generic.TemplateView):
    template_name = 'home.html'