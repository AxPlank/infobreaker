# Generated by Django 4.0.5 on 2022-07-06 13:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('board', '0004_alter_book_cnt_alter_book_stat_avg_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bookreview',
            name='content',
        ),
        migrations.AddField(
            model_name='bookreview',
            name='review',
            field=models.TextField(default=1),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='book',
            name='cnt',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='book',
            name='stat_avg',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='book',
            name='stat_sum',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
