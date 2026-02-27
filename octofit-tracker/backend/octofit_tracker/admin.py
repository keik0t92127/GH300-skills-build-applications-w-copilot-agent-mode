from django.contrib import admin
from .models import User, Team, Activity, Leaderboard, Workout


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ['username', 'email', 'first_name', 'last_name', 'is_active', 'date_joined']
    list_filter = ['is_active', 'date_joined']
    search_fields = ['username', 'email']
    ordering = ['-date_joined']


@admin.register(Team)
class TeamAdmin(admin.ModelAdmin):
    list_display = ['name', 'created_at']
    list_filter = ['created_at']
    search_fields = ['name']
    ordering = ['-created_at']


@admin.register(Activity)
class ActivityAdmin(admin.ModelAdmin):
    list_display = ['user_id', 'activity_type', 'duration_minutes', 'calories_burned', 'created_at']
    list_filter = ['activity_type', 'created_at']
    search_fields = ['user_id']
    ordering = ['-created_at']


@admin.register(Leaderboard)
class LeaderboardAdmin(admin.ModelAdmin):
    list_display = ['username', 'rank', 'total_activities', 'total_duration_minutes', 'total_calories_burned', 'updated_at']
    list_filter = ['rank', 'updated_at']
    search_fields = ['username', 'user_id']
    ordering = ['rank']


@admin.register(Workout)
class WorkoutAdmin(admin.ModelAdmin):
    list_display = ['name', 'difficulty', 'duration_minutes', 'created_at']
    list_filter = ['difficulty', 'created_at']
    search_fields = ['name']
    ordering = ['-created_at']
