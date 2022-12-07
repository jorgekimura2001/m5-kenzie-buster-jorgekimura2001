from django.db import models


class MovieRating(models.TextChoices):
    GENERAL = "G"
    PARENTAL_GUIDANCE = "PG"
    PARENTS_STRONGLY = "PG-13"
    RESTRICTED = "R"
    ADULTS_ONLY = "NC-17"


class Movie(models.Model):
    title = models.CharField(max_length=127)
    duration = models.CharField(max_length=10, null=True)
    rating = models.CharField(
        max_length=20,
        choices=MovieRating.choices,
        default=MovieRating.GENERAL,
    )
    synopsis = models.TextField(null=True)

    user = models.ForeignKey(
        "users.User",
        on_delete=models.CASCADE,
        related_name="movies",
    )

    users = models.ManyToManyField(
        'users.User', through='MovieOrder', related_name='movies_orders'
    )


class MovieOrder(models.Model):
    movie = models.ForeignKey(
        "movies.Movie",
        on_delete=models.CASCADE,
    )
    user = models.ForeignKey(
        "users.User",
        on_delete=models.CASCADE,
    )
    buyed_at = models.DateTimeField(auto_now_add=True)
    price = models.DecimalField(max_digits=8, decimal_places=2)
