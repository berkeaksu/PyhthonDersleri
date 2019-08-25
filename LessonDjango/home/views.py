from django.shortcuts import render
from django.http import HttpResponse
from .models import Slider

# Create your views here.
def index(request):
    # return HttpResponse("Welcome To Home Page")
    sliders = Slider.objects.all()
    return render(request, 'home/index.html', {'sliders': sliders})


def contact(request):
    return render(request, 'home/contact.html')