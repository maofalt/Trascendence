# Generated by Django 3.1.3 on 2024-02-18 14:36

from django.db import migrations, models
import django.db.models.deletion

def add_match_settings(apps, schema_editor):
    MatchSetting = apps.get_model('manage_tournament', 'MatchSetting')
    MatchSetting.objects.create(duration_sec=210, max_score=5, nbr_of_sets=1, paddle_speed=10, ball_speed=10, nbr_of_players=2)

class Migration(migrations.Migration):

    dependencies = [
        ('manage_tournament', '0005_auto_20240111_1801'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tournament',
            name='setting',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, to='manage_tournament.matchsetting'),
        ),
        migrations.RunPython(add_match_settings),
    ]
