from rest_framework.views import APIView, Request, Response, status
from .models import Movie
from .serializers import MovieSerializer, MovieOrderSerializer
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated
from .permissions import PermissionMovie
from django.shortcuts import get_object_or_404
from rest_framework.pagination import PageNumberPagination
import ipdb


class MovieView(APIView, PageNumberPagination):
    authentication_classes = [JWTAuthentication]
    permission_classes = [PermissionMovie]

    def get(self, request: Request) -> Response:
        movies = Movie.objects.all()
        movies_page = self.paginate_queryset(movies, request, view=self)
        serializer = MovieSerializer(movies_page, many=True)
        return self.get_paginated_response(serializer.data)

    def post(self, request: Request) -> Response:
        serializer = MovieSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(user=request.user)
        return Response(
            serializer.data,
            status.HTTP_201_CREATED,
        )


class MovieViewParams(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [PermissionMovie]

    def get(self, request: Request, movie_id: int) -> Response:
        movie = get_object_or_404(Movie, id=movie_id)
        serializer = MovieSerializer(movie)

        return Response(serializer.data, status.HTTP_200_OK)

    def delete(self, request: Request, movie_id: int) -> Response:
        movie = get_object_or_404(Movie, id=movie_id)
        movie.delete()

        return Response(status=status.HTTP_204_NO_CONTENT)


class MovieOrderView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self, request: Request, movie_id: int) -> Response:
        movie = get_object_or_404(Movie, id=movie_id)
        serializer = MovieOrderSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(movie=movie, user=request.user)

        return Response(
            serializer.data,
            status.HTTP_201_CREATED,
        )
