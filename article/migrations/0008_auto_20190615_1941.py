# Generated by Django 2.2.1 on 2019-06-15 10:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0007_auto_20190614_1729'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='season',
            name='explain_in_1_line',
        ),
        migrations.AddField(
            model_name='season',
            name='think_this_again',
            field=models.CharField(blank=True, default='', max_length=400),
        ),
    ]