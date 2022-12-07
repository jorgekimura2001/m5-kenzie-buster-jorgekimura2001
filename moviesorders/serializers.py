from rest_framework import serializers
from .models import MovieOrder


class MovieOrderSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    buyed_at = serializers.DateTimeField(read_only=True)
    price = serializers.DecimalField(max_digits=8, decimal_places=2)
    buyed_by = serializers.SerializerMethodField()
    title = serializers.SerializerMethodField()

    def get_buyed_by(self, obj):
        ...

    def get_title(self, obj):
        ...

    def create(self, validated_data: dict):
        return MovieOrder.objects.create(**validated_data)
