from django.shortcuts import render
from django.http import Http404

from .models import Year, Season, Article

def base(request):
    return render(request, "base.html", {
        'years':Year.objects.all(),
        'seasons':Season.objects.all
    })

