from django.db import models
# from mptt.models import MPTTModel, TreeForeignKey
from tinymce.models import HTMLField


class Year(models.Model):
    YEAR_CHOICES = (
        ('19', '2019'),
        ('20', '2020'),
        ('21', '2021'),
        ('22', '2022'),
        ('23', '2023'),
        ('24', '2024'),
        ('25', '2025'),
    )

    name = models.CharField(max_length=4, choices=YEAR_CHOICES, default='2019')

    def __str__(self):
        return self.name

class Season(models.Model):
    SEASON_CHOICES = (
        ('spr', 'SPRING'),
        ('sum', 'SUMMER'),
        ('aut', 'AUTUMN'),
        ('win', 'WINTER'),
    )

    name = models.CharField(max_length=4, choices=SEASON_CHOICES, default='1')
    year = models.ForeignKey(Year, on_delete=models.CASCADE,
                             related_name='seasons')

    def __str__(self):
        return '{0} {1}'.format(self.year.name, self.name)
        # return self.year.name, self.name


class Article(models.Model):
    title = models.CharField(max_length=12, default='제목쓰셈')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    content = HTMLField()
    season = models.ForeignKey(
        Season,
        related_name='article',
        on_delete=models.CASCADE
    )

    def __str__(self):
        return self.title