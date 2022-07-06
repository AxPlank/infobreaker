# Generated by Django 4.0.5 on 2022-07-06 10:57

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('board', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='BookReview',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField(null=True)),
                ('create_date', models.DateField()),
            ],
        ),
        migrations.AddField(
            model_name='book',
            name='cnt',
            field=models.FloatField(null=True),
        ),
        migrations.AddField(
            model_name='book',
            name='stat',
            field=models.IntegerField(null=True),
        ),
        migrations.DeleteModel(
            name='Review',
        ),
        migrations.AddField(
            model_name='bookreview',
            name='book',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='board.book'),
        ),
        migrations.AddField(
            model_name='bookreview',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
