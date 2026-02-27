from rest_framework import serializers
from .models import User, Team, Activity, Leaderboard, Workout


class UserSerializer(serializers.ModelSerializer):
    """Serializer for User model"""
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'first_name', 'last_name', 'is_active', 'date_joined']
        read_only_fields = ['id', 'date_joined']


class TeamSerializer(serializers.ModelSerializer):
    """Serializer for Team model"""
    class Meta:
        model = Team
        fields = ['id', 'name', 'description', 'created_at', 'members']
        read_only_fields = ['id', 'created_at']


class ActivitySerializer(serializers.ModelSerializer):
    """Serializer for Activity model"""
    class Meta:
        model = Activity
        fields = ['id', 'user_id', 'activity_type', 'duration_minutes', 'calories_burned', 'distance_km', 'created_at']
        read_only_fields = ['id', 'created_at']


class LeaderboardSerializer(serializers.ModelSerializer):
    """Serializer for Leaderboard model"""
    class Meta:
        model = Leaderboard
        fields = ['id', 'user_id', 'username', 'team_id', 'total_activities', 'total_duration_minutes', 'total_calories_burned', 'rank', 'updated_at']
        read_only_fields = ['id', 'updated_at']


class WorkoutSerializer(serializers.ModelSerializer):
    """Serializer for Workout model"""
    class Meta:
        model = Workout
        fields = ['id', 'name', 'description', 'difficulty', 'duration_minutes', 'exercises', 'created_at']
        read_only_fields = ['id', 'created_at']
