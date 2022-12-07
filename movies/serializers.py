from rest_framework import serializers
from .models import MovieRating, Movie, MovieOrder
import ipdb


class MovieSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField(max_length=127)
    duration = serializers.CharField(
        max_length=127,
        allow_null=True,
        required=False,
    )
    rating = serializers.ChoiceField(
        choices=MovieRating.choices,
        default=MovieRating.GENERAL,
    )
    synopsis = serializers.CharField(
        allow_null=True,
        required=False,
    )
    added_by = serializers.SerializerMethodField(read_only=True)

    def get_added_by(self, obj):
        return obj.user.email

    def create(self, validated_data: dict):
        return Movie.objects.create(**validated_data)


class MovieOrderSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    buyed_at = serializers.DateTimeField(read_only=True)
    price = serializers.DecimalField(max_digits=8, decimal_places=2)
    buyed_by = serializers.SerializerMethodField()
    title = serializers.SerializerMethodField()

    def get_buyed_by(self, obj):
        return obj.user.email

    def get_title(self, obj):
        return obj.movie.title

    def create(self, validated_data: dict):
        return MovieOrder.objects.create(**validated_data)
