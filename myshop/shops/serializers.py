from rest_framework import serializers
from .models import Shop

class ShopSerializer(serializers.ModelSerializer):
    class Meta:
        model = Shop
        fields = ['id', 'name', 'latitude', 'longitude']

    def validate_latitude(self, value):
        if value < -90 or value > 90:
            raise serializers.ValidationError("Latitude must be between -90 and 90.")
        return value

    def validate_longitude(self, value):
        if value < -180 or value > 180:
            raise serializers.ValidationError("Longitude must be between -180 and 180.")
        return value
class ShopWithDistanceSerializer(ShopSerializer):
    distance = serializers.FloatField()  # Add distance field

    class Meta(ShopSerializer.Meta):
        fields = ShopSerializer.Meta.fields + ['distance']  