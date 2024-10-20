from django.shortcuts import render

# Create your views here.
from rest_framework import generics
from rest_framework import status

from rest_framework.response import Response
from .models import Shop
from .serializers import ShopSerializer
from .serializers import ShopWithDistanceSerializer
from django.db.models import F
import math
from .utils import haversine
class ShopCreateView(generics.CreateAPIView):
    queryset = Shop.objects.all()
    serializer_class = ShopSerializer

class ShopSearchView(generics.ListCreateAPIView):
    queryset = Shop.objects.all()
    serializer_class = ShopSerializer

    def get(self, request, *args, **kwargs):
        lat = request.query_params.get('lat')
        lon = request.query_params.get('lon')

        if lat is not None and lon is not None:
            shops = self.get_queryset()  # Get all shops
            shops_with_distance = []

            # Calculate distance for each shop
            for shop in shops:
                distance = haversine(float(lat), float(lon), shop.latitude, shop.longitude)
                shops_with_distance.append({
                    'shop': shop,
                    'distance': distance
                })

            # Sort by distance
            shops_with_distance.sort(key=lambda x: x['distance'])

            # Prepare the response data
            response_data = [
                {
                    'name': shop_distance['shop'].name,
                    'latitude': shop_distance['shop'].latitude,
                    'longitude': shop_distance['shop'].longitude,
                    'distance': shop_distance['distance']
                }
                for shop_distance in shops_with_distance
            ]

            return Response(response_data, status=status.HTTP_200_OK)

        return Response({"error": "Latitude and Longitude are required."}, status=status.HTTP_400_BAD_REQUEST)

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)