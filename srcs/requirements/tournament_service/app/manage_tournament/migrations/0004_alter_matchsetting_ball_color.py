# Generated by Django 5.0.4 on 2024-04-20 20:39

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('manage_tournament', '0003_alter_tournament_tournament_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='matchsetting',
            name='ball_color',
            field=models.CharField(default='0x000000', max_length=8, validators=[django.core.validators.RegexValidator('^0x(?:[0-9a-fA-F]{3}){1,2}$', message='Invalid color format.')]),
        ),
    ]
