# Generated by Django 4.0.5 on 2022-06-16 05:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('exam', '0010_alter_problem_ex1_alter_problem_ex2_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='problem',
            name='example',
            field=models.ImageField(blank=True, null=True, upload_to='<django.db.models.fields.CharField>/<django.db.models.fields.IntegerField>/'),
        ),
    ]
