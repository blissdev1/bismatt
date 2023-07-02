from django.http import JsonResponse
from django.shortcuts import redirect, render
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from .forms import CarForm, CreationForm
from django.contrib import messages
from Cars.models import Car
import json
from random import shuffle

# Create your views here.



def home_view(request): 
  context = {}
  return render(request, "home.html", context)
  
 
def car_view(request): 
  cars = Car.objects.all()
  random_cars = list(cars)
  shuffle(random_cars)
  context = {
    'cc': random_cars
  }
  return render(request, "car.html", context)
  
  
def ecar_view(request, pk):
  single_car = Car.objects.get(id=pk)
  cars = Car.objects.all()
  random_car = list(cars)
  shuffle(random_car)
  context = {
    "each": single_car, 
    "all": random_car
  }
#  a = Text.objects.get(id=pk)
#  context = {"all": a}
  return render(request, 'ecar.html', context)


def create_user_view(request):
  form = CreationForm()
  if request.method == "POST":
    form = CreationForm(request.POST)
    if form.is_valid():
     form.save()
     user = form.cleaned_data.get('username')
     messages.success(request, "Account was created for " + user)
     return redirect("login")

  context = {"form":form}
  return render(request, "registrations/create_user.html", context)


def login_view(request):

  if request.method == "POST":
    username = request.POST.get('username')
    password = request.POST.get('password')

    user = authenticate(request, username=username, password=password)

    if user is not None:
      login(request, user)
      return redirect('home')
    else:
      messages.info(request, "Username or Password is incorrect")
  context = {}
  return render(request, "registrations/login.html", context)

def logout_view(request):
  logout(request)
  return redirect('login')

def search_view(request):
  if request.method == "POST":
    searched_data = request.POST["searched_data"]
    cars = Car.objects.filter(model__contains=searched_data)
    context = {"cars_result": cars}
    return render(request, "search.html", context)
  
def contact_view(request):
    return render(request, "contact.html")
  
def about_view(request):
    return render(request, "about.html")

def json_view(request):
  data = list(Car.objects.values())
  return JsonResponse(data, safe=False)

