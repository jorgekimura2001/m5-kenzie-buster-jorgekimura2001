from rest_framework import serializers
from .models import MovieRating, Movie
from users.models import User
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
        return Movie.objects.create(
            **validated_data,
        )
