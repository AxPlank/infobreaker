# Generated by Django 4.0.5 on 2022-07-06 14:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('exam', '0017_alter_problem_answer_alter_problem_ex1_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='problem',
            name='example',
            field=models.ImageField(blank=True, null=True, upload_to='media/problem/<django.db.models.fields.CharField>/<django.db.models.fields.IntegerField>/'),
        ),
    ]