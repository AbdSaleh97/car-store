
from django.contrib import admin
from django.urls import path
from .views import HomeView,CarListView,CarDetails,CreateCar,CarUpdateView,CarDeleteView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',HomeView.as_view(), name='home'),
    path('car_list',CarListView.as_view(), name='cars'),
    path('car_details/<int:pk>',CarDetails.as_view(), name='details'),
    path('create_car', CreateCar.as_view(), name='create'),
    path('car_list/<int:pk>',CarUpdateView.as_view(),name='update'),
     path('delete/<int:pk>', CarDeleteView.as_view(), name="delete")
]