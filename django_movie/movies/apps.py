from django.apps import AppConfig


class MoviesConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'movies'
    verbose_name = 'Фильмы'     # название apps в админке. все модели этого apps будут внутри этой группы
