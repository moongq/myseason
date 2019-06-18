from django.contrib import admin

from .models import Year, Article, Season

admin.site.register(Year)
admin.site.register(Article)


@admin.register(Season)
class SeasonAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'year', 'explain_little']
    list_display_links = ['id', 'name']

    def explain_little(self, season):
        return '{0}'.format(season.think_this_again[0:10])
    explain_little.short_description = 'explain'