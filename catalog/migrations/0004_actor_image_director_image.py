# Generated by Django 4.2.7 on 2023-12-10 10:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0003_actor_best_actor_data_actor_filmcount_director_best_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='actor',
            name='image',
            field=models.URLField(blank=True, null=True, verbose_name='Фото'),
        ),
        migrations.AddField(
            model_name='director',
            name='image',
            field=models.URLField(blank=True, null=True, verbose_name='Фото'),
        ),
    ]
