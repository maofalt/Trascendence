from rest_framework import serializers
from .models import Tournament, TournamentMatch, MatchSetting, GameType, TournamentType
from .models import RegistrationType, TournamentPlayer, Player, MatchParticipants

class MatchSettingSerializer(serializers.ModelSerializer):
    class Meta:
        model = MatchSetting
        fields = fields = '__all__'

class TournamentSerializer(serializers.ModelSerializer):
    setting = MatchSettingSerializer()
    is_full = serializers.SerializerMethodField()
    joined = serializers.SerializerMethodField()

    class Meta:
        model = Tournament
        fields = ['id', 'tournament_name', 'nbr_of_player_total', 'nbr_of_player_match', 'setting', 'registration_period_min', 'host_id', 'joined', 'is_full' ]

    def create(self, validated_data):
        setting_data = validated_data.pop('setting')  # Extract data from MatchSetting
        setting = MatchSetting.objects.create(**setting_data)  # Create a new MatchSetting object
        tournament = Tournament.objects.create(setting=setting, **validated_data)  # Create a new Tournament object

        return tournament

    def update(self, instance, validated_data):
        setting_data = validated_data.pop('setting')
        setting = instance.setting

        instance.id = validated_data.get('id', instance.id)
        instance.tournament_name = validated_data.get('tournament_name', instance.tournament_name)
        instance.nbr_of_player_total = validated_data.get('nbr_of_player_total', instance.nbr_of_player_total)
        instance.nbr_of_player_match = validated_data.get('nbr_of_player_match', instance.nbr_of_player_match)
        instance.registration_period_min = validated_data.get('registration_period_min', instance.registration_period_min)
        instance.host_id = validated_data.get('host_id', instance.host_id)
        instance.save()

        # `MatchSetting` is a one-to-one relationship with `Tournament`
        for field, value in setting_data.items():
            setattr(setting, field, value)
        setting.save()

        return instance

    def get_joined(self, obj):
        return obj.players.count()

    def get_is_full(self, obj):
        return obj.is_full()

class TournamentRegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = TournamentPlayer
        fields = ['tournament_id', 'player'] # Fields to be serialized

    def create(self, validated_data):
        # Create a new TournamentPlayer object
        tournament_player = TournamentPlayer.objects.create(**validated_data)
        return tournament_player

class PlayerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Player
        fields = ['id', 'total_played', 'won_match', 'won_tournament']

class MatchParticipantsSerializer(serializers.ModelSerializer):
    class Meta:
        model = MatchParticipants
        fields = ['id', 'match_id', 'round_number', 'player_id', 'is_winner']

class MatchGeneratorSerializer(serializers.Serializer):
    tournament_id = serializers.IntegerField()
    class Meta:
        model = Tournament
        fields = ['id']

    def create(self, validated_data):
        tournament_id = validated_data.get('tournament_id')
        return tournament_id

    def update(self, instance, validated_data):
        instance.tournament_id = validated_data.get('tournament_id', instance.tournament_id)
        return instance

# class GameTypeSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = GameType
#         fields = ['id', 'type_name']

class TournamentMatchSerializer(serializers.ModelSerializer):
    players = PlayerSerializer(many=True)
    participants = MatchParticipantsSerializer(many=True)

    class Meta:
        model = TournamentMatch
        fields = ['id', 'state', 'tournament_id', 'round_number', 'match_time', 'players', 'participants']

class gamemodeDataSerializer(serializers.ModelSerializer):
    nbrOfPlayers = serializers.IntegerField() # it is returning not a nbr_of_player for match setting, it returns actaul number of payer for a current match
    nbrOfRounds = serializers.IntegerField(source='round_number') #assume it is for current round number

    def get_nbrOfPlayers(self, obj):
        return obj.players.count()

class fieldDataSerializer(serializers.ModelSerializer):
	wallsFactor = serializers.IntegerField(source='walls_factor')
    sizeOfGoals = serializers.IntegerField(source='size_of_goals')

class paddlesDataSerializer(serializers.ModelSerializer):
    width = serializers.IntegerField(default=2)
    height = serializers.IntegerField(source='paddle_height')
    speed = serializers.DecimalField(source='paddle_speed')
    
class ballDataSerializer(serializers.ModelSerializer):
    speed = serializers.DecimalField(source='ball_speed')
    radius = serializers.DecimalField(source='ball_radius')
    color = serializers.CharField(source='ball_color')


class TournamentMatchRoundSerializer(serializers.ModelSerializer):
    players = PlayerSerializer(many=True)
    match_id = serializers.IntegerField(source='id')

    class Meta:
        model = TournamentMatch
        fields = ['tournament_id', 'match_id', 'gamemodeData', 'fieldData', 'paddlesData', 'ballData', 'players']


# class TournamentTypeSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = TournamentType
#         fields = ['id', 'type_name']

# class RegistrationTypeSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = RegistrationType
#         fields = ['id', 'type_name']

class TournamentPlayerSerializer(serializers.ModelSerializer):
    # username = serializers.CharField()
    players = PlayerSerializer(many=True)
    class Meta:
        model = TournamentPlayer
        fields = ['tournament_id', 'players']

class SimpleTournamentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tournament
        fields = ['id', 'tournament_name']

class SimpleMatchSerializer(serializers.ModelSerializer):
    winner_id = serializers.SerializerMethodField()

    class Meta:
        model = TournamentMatch
        fields = ['id', 'tournament_id', 'round_number', 'players', 'winner_id']

    def get_winner_id(self, obj):
        winner = obj.participants.filter(is_winner=True).first()
        if winner:
            return winner.player_id
        return None


class PlayerGameStatsSerializer(serializers.Serializer):
    played_tournaments = SimpleTournamentSerializer(many=True, read_only=True)
    played_matches = SimpleMatchSerializer(many=True, read_only=True)

    total_played = serializers.IntegerField()
    nbr_of_lost_matches = serializers.IntegerField()
    nbr_of_won_matches = serializers.IntegerField()
    nbr_of_won_tournaments = serializers.IntegerField()
    # average_score = serializers.DecimalField(max_digits=5, decimal_places=2)
    # highest_score = serializers.IntegerField()