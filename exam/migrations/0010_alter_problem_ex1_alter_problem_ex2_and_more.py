# Generated by Django 4.0.5 on 2022-06-16 04:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('exam', '0009_alter_problem_ex1_alter_problem_ex2_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='problem',
            name='ex1',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='problem',
            name='ex2',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='problem',
            name='ex3',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='problem',
            name='ex4',
            field=models.TextField(blank=True),
        ),
    ]
