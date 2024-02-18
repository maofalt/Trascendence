# Generated by Django 3.1.3 on 2024-01-11 17:19

from django.db import migrations

def add_game_types(apps, schema_editor):
    GameType = apps.get_model('manage_tournament', 'GameType')
    GameType.objects.create(type_name='gametype1')
    GameType.objects.create(type_name='gametype2')
    GameType.objects.create(type_name='gametype3')


class Migration(migrations.Migration):

    dependencies = [
        ('manage_tournament', '0002_auto_20240110_2131'),
    ]

    operations = [
        migrations.RunPython(add_game_types),
    ]
