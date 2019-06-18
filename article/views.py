from django.shortcuts import render

from .models import Year, Season, Article


def first_view(request):
    return render(request, "first_view.html", {
        'years':Year.objects.all(),
        'seasons':Season.objects.all()
    })


def each_season(request, season_id):
    season_articles = Article.objects.filter(season_id=season_id)
    exact_season = Season.objects.get(id=season_id)
    return render(request, "each_season.html", {
        'years': Year.objects.all(),
        'season': exact_season,
        'articles':season_articles
    })