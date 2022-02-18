from django.contrib import admin
from .models import Category, Genre, Movie, MovieShots, Actor, Rating, RatingStar, Reviews


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    """Категории"""
    list_display = ('id', 'name', 'url')
    list_display_links = ('name', )

# admin.site.register(Category, CategoryAdmin)


class ReviewInline(admin.TabularInline):    # еще есть StackedInline
    """Отзывы на странице фильма"""
    model = Reviews
    extra = 1
    readonly_fields = ('name', 'email')


@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    """Фильмы"""
    list_display = ('title', 'category', 'url', 'draft')
    list_filter = ('category', 'year')
    search_fields = ('title', 'category__name')     # category__name - по какому именно атрибуту класса Category ищем
    inlines = [ReviewInline]    # в фильме отображатся все отзывы к нему
    save_on_top = True
    save_as = True      # добавляет в админку кнопку "Сохранить как новый объект"
    list_editable = ('draft',)
    fieldsets = (
        (None, {
            'fields': (('title', 'tagline'), )
        }),
        (None, {
            'fields': ('description', 'poster')
        }),
        (None, {
            'fields': (('year', 'world_premiere', 'country'),)
        }),
        ("Actors", {
            'classes': ('collapse',),   # сворачиват данные поля
            'fields': (("actors", "directors", "genres", "category"), )
        }),
        (None, {
            'fields': (("budget", "fees_in_usa", "fees_in_world"),)
        }),
        ("Options", {
            'fields': (("url", "draft"),)
        }),
    )

@admin.register(Reviews)
class ReviewAdmin(admin.ModelAdmin):
    """Отзывы"""
    list_display = ('name', 'email', 'parent', 'movie', 'id')
    readonly_fields = ('name', 'email')     # эти поля нельзя редактировать из админки

@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    """Жанры"""
    list_display = ('name', 'url')

@admin.register(Actor)
class ActorAdmin(admin.ModelAdmin):
    """Актеры"""
    list_display = ('name', 'age')


@admin.register(Rating)
class RatingAdmin(admin.ModelAdmin):
    """Рейтинг"""
    list_display = ('name', 'ip')

@admin.register(MovieShots)
class MovieShotsAdmin(admin.ModelAdmin):
    """Кадры из фильма"""
    list_display = ('ip', 'movie', 'star')


admin.site.register(RatingStar)
