from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

def menu(request):
    return render(request, 'menu.html')

def about(request):
    return render(request, 'about.html')


from django.http import HttpResponseRedirect,HttpResponse
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic
from django.utils import timezone


class IndexView(generic.ListView):
    template_name = 'loth/index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        return render.objects.order_by('-pub_date')[:5]

class MenuView(generic.ListView):
    template_name = 'loth/menu.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        return render.objects.order_by('-pub_date')[:5]
