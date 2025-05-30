from rest_framework import serializers

from .models import Competitor, Debate, Judge, Score, Tournament


class TournamentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tournament
        fields = "__all__"  # Includes all model fields


class DebateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Debate
        fields = "__all__"


class JudgeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Judge
        fields = "__all__"


class CompetitorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Competitor
        fields = "__all__"


class ScoreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Score
        fields = "__all__"
