# Generated by Django 4.0.5 on 2022-07-07 12:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('board', '0007_alter_book_cover_img'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='cnt',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
