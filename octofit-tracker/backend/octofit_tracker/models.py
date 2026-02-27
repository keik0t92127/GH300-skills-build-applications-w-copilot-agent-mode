from django.db import models
from django.contrib.auth.models import User as DjangoUser
from djongo import models as djongo_models


class User(djongo_models.Model):
    """User model for OctoFit Tracker"""
    username = models.CharField(max_length=150, unique=True)
    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=30, blank=True)
    last_name = models.CharField(max_length=30, blank=True)
    is_active = models.BooleanField(default=True)
    date_joined = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        db_table = 'users'
    
    def __str__(self):
        return self.username


class Team(djongo_models.Model):
    """Team model for OctoFit Tracker"""
    name = models.CharField(max_length=200, unique=True)
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    members = models.JSONField(default=list, blank=True)  # List of user IDs
    
    class Meta:
        db_table = 'teams'
    
    def __str__(self):
        return self.name


class Activity(djongo_models.Model):
    """Activity model for OctoFit Tracker"""
    ACTIVITY_TYPES = [
        ('running', 'Running'),
        ('cycling', 'Cycling'),
        ('swimming', 'Swimming'),
        ('weightlifting', 'Weightlifting'),
        ('yoga', 'Yoga'),
        ('other', 'Other'),
    ]
    
    user_id = models.CharField(max_length=150)
    activity_type = models.CharField(max_length=50, choices=ACTIVITY_TYPES)
    duration_minutes = models.IntegerField()
    calories_burned = models.FloatField()
    distance_km = models.FloatField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        db_table = 'activities'
    
    def __str__(self):
        return f"{self.user_id} - {self.activity_type} on {self.created_at}"


class Leaderboard(djongo_models.Model):
    """Leaderboard model for OctoFit Tracker"""
    user_id = models.CharField(max_length=150)
    username = models.CharField(max_length=150)
    team_id = models.CharField(max_length=200, null=True, blank=True)
    total_activities = models.IntegerField(default=0)
    total_duration_minutes = models.IntegerField(default=0)
    total_calories_burned = models.FloatField(default=0.0)
    rank = models.IntegerField(null=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        db_table = 'leaderboard'
    
    def __str__(self):
        return f"{self.username} - Rank {self.rank}"


class Workout(djongo_models.Model):
    """Workout model for suggested workouts"""
    DIFFICULTY_LEVELS = [
        ('beginner', 'Beginner'),
        ('intermediate', 'Intermediate'),
        ('advanced', 'Advanced'),
    ]
    
    name = models.CharField(max_length=200)
    description = models.TextField()
    difficulty = models.CharField(max_length=50, choices=DIFFICULTY_LEVELS)
    duration_minutes = models.IntegerField()
    exercises = models.JSONField(default=list)  # List of exercise objects
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        db_table = 'workouts'
    
    def __str__(self):
        return self.name
