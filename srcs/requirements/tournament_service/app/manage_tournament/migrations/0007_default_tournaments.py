# Generated by Django 5.0.3 on 2024-03-31 13:29
import django.core.validators
import random
from django.db import migrations, models
from django.utils import timezone
from manage_tournament.models import Tournament, MatchSetting

def create_random_game_setting(account_id):
    game_setting = {
        "nbr_of_player": random.randint(2, 8),
        "max_score": random.randint(1, 10),
        "duration_sec": random.randint(1, 99),
        "walls_factor": round(random.uniform(0, 2), 2),
        "size_of_goals": random.randint(15, 30),
        "paddle_height": random.randint(1, 12),
        "paddle_speed": round(random.uniform(0.1, 3), 2),
        "ball_speed": round(random.uniform(0.1, 3), 2),
        "ball_radius": round(random.uniform(0.5, 7), 2),
        "ball_color": "0x00ffff",
        "nbr_of_rounds": 5,
        "ball_texture": '',
        "ball_model": '',
    }

    return game_setting


def create_tournament(apps, schema_editor):
    Player = apps.get_model('manage_tournament', 'Player')
    MatchSetting = apps.get_model('manage_tournament', 'MatchSetting')
    Tournament = apps.get_model('manage_tournament', 'Tournament')

    players = ['motero', 'jisu', 'znogueira', 'amanda', 'yoel', 'motero2', 'jisu2', 'znogueira2', 'amanda2', 'yoel2']
    for i, player_username in enumerate(players):
        #create player or get it if it already exists
        host_player, _ = Player.objects.get_or_create(id=i+1, username=player_username, defaults={'total_played': 0})

        #generate random game setting
        game_setting = create_random_game_setting(host_player.id)
        match_setting = MatchSetting.objects.create(**game_setting)

        #create tournament
        nbr_of_players_total = random.randint(game_setting['nbr_of_player'], 20)
        tournament = Tournament.objects.create(
            tournament_name=f'TEST_{i+1}',
            nbr_of_player_total=nbr_of_players_total,
            nbr_of_player_match=game_setting['nbr_of_player'],
            setting=match_setting,
            registration_period_min=random.randint(5, 60),
            host=host_player,
        )

        #add host player to the tournament
        tournament.players.add(host_player)
        nbr_of_players_assigned = min(len(players), nbr_of_players_total)
        print(f'Nbr of players total: {nbr_of_players_total}  /  len(players): {len(players)}')
        print(f'Nbr of players assigned: {nbr_of_players_assigned}')
        for j, player_username in enumerate(players):
            if player_username != host_player.username and j < nbr_of_players_assigned:
                player, _ = Player.objects.get_or_create(id=j+1, username=player_username, defaults={'total_played': 0})
                tournament.players.add(player)
                tournament.save()
        print(f'Tournament {tournament.tournament_name} created with host player {host_player.username}')

class Migration(migrations.Migration):

    dependencies = [
        ('manage_tournament', '0006_matchsetting_ball_model_matchsetting_ball_texture_and_more'),
    ]

    operations = [
        migrations.RunPython(create_tournament),
    ]