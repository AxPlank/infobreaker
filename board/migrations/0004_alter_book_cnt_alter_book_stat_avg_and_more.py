# Generated by Django 4.0.5 on 2022-07-06 11:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('board', '0003_remove_book_stat_book_stat_avg_book_stat_sum_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='cnt',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='book',
            name='stat_avg',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='book',
            name='stat_sum',
            field=models.IntegerField(null=True),
        ),
    ]
