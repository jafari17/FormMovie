# Generated by Django 4.2.3 on 2023-07-28 10:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('movie_name', models.CharField(max_length=100)),
                ('director', models.CharField(max_length=100)),
                ('release_date', models.IntegerField()),
                ('Genre', models.CharField(max_length=100)),
                ('imdb', models.IntegerField()),
            ],
        ),
    ]
