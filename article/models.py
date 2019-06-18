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
        return self.get_name_display()


class Season(models.Model):
    name = models.CharField(max_length=40, default='새 시즌')
    year = models.ForeignKey(Year, on_delete=models.CASCADE,
                             related_name='seasons')
    # 계절의 목표를 each_season 맨위에 보이면 어떨까 싶음. 그래서 모델을 새로 만들고 새로 해야할듯?
    think_this_again = models.CharField(max_length=400, default='', blank=True)

    def __str__(self):
        return '{0}_'.format(self.name)
        # '{0} {1}'.format(self.year.name, self.name) 6.10 수정전
        # return self.year.name, self.name



class Article(models.Model):
    title = models.CharField(max_length=12, default='null')
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