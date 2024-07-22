from django.shortcuts import render
from django.views.generic import TemplateView, ListView, DetailView,CreateView,UpdateView,DeleteView
from .models import Car
from django.urls import reverse_lazy

# Create your views here.
class HomeView(TemplateView):
    template_name = "home.html"

class CarListView(ListView):
    model = Car
    template_name = "car_list.html"
    context_object_name = 'Car'

class CarDetails(DetailView):
    model = Car
    template_name = 'car_details.html'
    context_object_name = 'Car'

class CreateCar(CreateView):
    model = Car
    template_name = 'create_car.html'
    fields = ["buyer",
            "car_model",
            "car_brand",
            "car_price",
            "is_bought"]
    
class CarUpdateView(UpdateView):
    model = Car
    template_name="car_update.html"
    fields = "__all__"

class CarDeleteView(DeleteView):
    model=Car
    template_name='car_delete.html'
    success_url = reverse_lazy('cars')

