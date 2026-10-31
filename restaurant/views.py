from django.http import JsonResponse
from django.shortcuts import render
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from .models import Booking, Menu
from .serializers import bookingSerializer, menuSerializer

# Create your views here.

@api_view()
@permission_classes([IsAuthenticated])
def securedView(request):
    return Response({"message": "Hello, World!"})

class Bookingview(APIView):
    def get(self, request, format=None):
        items = Booking.objects.all()
        serializer = bookingSerializer(items, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = bookingSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)


class MenuItemsView(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Menu.objects.all()
    serializer_class = menuSerializer


class SingleMenuItemView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Menu.objects.all()
    serializer_class = menuSerializer


def sayHello(request):
    return JsonResponse({"message": "Hello, World!"})

def index(request):
    return render(request, 'index.html', {})