# Generated by Django 3.1.3 on 2024-01-10 21:31

from django.db import migrations

def add_game_types(apps, schema_editor):
    GameType = apps.get_model('manage_tournament', 'GameType')

    game_type1 = GameType(type_name='tata')
    game_type2 = GameType(type_name='toto')
    
    game_type1.save()
    game_type2.save()

class Migration(migrations.Migration):

    dependencies = [
        ('manage_tournament', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='matchparticipants',
            old_name='participant_sacore',
            new_name='participant_score',
        ),
        migrations.RunPython(add_game_types),
    ]
