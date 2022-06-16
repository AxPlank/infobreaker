# Generated by Django 4.0.5 on 2022-06-16 00:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('exam', '0004_practicalpart_writtenpart'),
    ]

    operations = [
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(max_length=255)),
                ('part', models.IntegerField()),
                ('question', models.TextField()),
                ('example', models.ImageField(blank=True, upload_to='written/5/')),
                ('ex1', models.TextField()),
                ('ex2', models.TextField()),
                ('ex3', models.TextField()),
                ('ex4', models.TextField()),
                ('answer', models.IntegerField()),
                ('comment', models.TextField()),
            ],
        ),
        migrations.DeleteModel(
            name='PracticalQuestion',
        ),
        migrations.DeleteModel(
            name='WrittenQuestion',
        ),
    ]
