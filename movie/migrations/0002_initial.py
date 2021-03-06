# Generated by Django 4.0.5 on 2022-06-13 11:55

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('movie', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='moviemodel',
            name='like_users',
            field=models.ManyToManyField(blank=True, null=True, related_name='like_articles', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='moviecomment',
            name='movie',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='movie.moviemodel'),
        ),
        migrations.AddField(
            model_name='moviecomment',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
