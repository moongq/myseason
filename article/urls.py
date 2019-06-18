from django.urls import path, include, re_path
from . import views

urlpatterns = [
    path('', views.first_view),
    path('each_season/<int:season_id>', views.each_season, name='each_season'),

]
