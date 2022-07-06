# Generated by Django 4.0.5 on 2022-07-06 11:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('board', '0002_bookreview_book_cnt_book_stat_delete_review_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='book',
            name='stat',
        ),
        migrations.AddField(
            model_name='book',
            name='stat_avg',
            field=models.FloatField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='book',
            name='stat_sum',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='bookreview',
            name='stat',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='book',
            name='cnt',
            field=models.FloatField(default=1),
            preserve_default=False,
        ),
    ]