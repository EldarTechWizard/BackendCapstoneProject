from django.shortcuts import render
from .serializers import MenuSerializer,BookingSerializer
from rest_framework import generics
from rest_framework.viewsets import ModelViewSet 
from .models import Menu,Booking

# Create your views here. 
class BookingViewClass(ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
class MenuItemsView(generics.ListCreateAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer

class SingleMenuItemView(generics.RetrieveUpdateAPIView, generics.DestroyAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer

def index(request):
    return render(request, 'index.html', {})