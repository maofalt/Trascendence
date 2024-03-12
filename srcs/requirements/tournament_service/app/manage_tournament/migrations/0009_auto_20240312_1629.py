# Generated by Django 3.1.3 on 2024-03-12 16:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('manage_tournament', '0008_auto_20240224_1405'),
    ]

    operations = [
        migrations.AlterField(
            model_name='matchsetting',
            name='ball_speed',
            field=models.FloatField(default=0.2),
        ),
        migrations.AlterField(
            model_name='matchsetting',
            name='paddle_speed',
            field=models.FloatField(default=0.5),
        ),
    ]
