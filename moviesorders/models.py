from django.db import models


class MovieOrder(models.Model):
    movies = models.ForeignKey(
        'movies.Movie',
        on_delete=models.CASCADE,
        related_name='movie_order'
    )
    users = models.ForeignKey(
        'users.User',
        on_delete=models.CASCADE,
        related_name='movie_order'
    )
    buyed_at = models.DateTimeField(auto_now_add=True)
    price = models.DecimalField(max_digits=8, decimal_places=2)