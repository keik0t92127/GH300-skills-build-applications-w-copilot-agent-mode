from rest_framework import viewsets, status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import User, Team, Activity, Leaderboard, Workout
from .serializers import UserSerializer, TeamSerializer, ActivitySerializer, LeaderboardSerializer, WorkoutSerializer


@api_view(['GET'])
def api_root(request):
    """API root endpoint that lists all available endpoints"""
    return Response({
        'message': 'Welcome to OctoFit Tracker API',
        'version': '1.0.0',
        'endpoints': {
            'users': request.build_absolute_uri('/api/users/'),
            'teams': request.build_absolute_uri('/api/teams/'),
            'activities': request.build_absolute_uri('/api/activities/'),
            'leaderboard': request.build_absolute_uri('/api/leaderboard/'),
            'workouts': request.build_absolute_uri('/api/workouts/'),
        }
    })


class UserViewSet(viewsets.ModelViewSet):
    """ViewSet for User model"""
    queryset = User.objects.all()
    serializer_class = UserSerializer


class TeamViewSet(viewsets.ModelViewSet):
    """ViewSet for Team model"""
    queryset = Team.objects.all()
    serializer_class = TeamSerializer


class ActivityViewSet(viewsets.ModelViewSet):
    """ViewSet for Activity model"""
    queryset = Activity.objects.all()
    serializer_class = ActivitySerializer


class LeaderboardViewSet(viewsets.ModelViewSet):
    """ViewSet for Leaderboard model"""
    queryset = Leaderboard.objects.all()
    serializer_class = LeaderboardSerializer


class WorkoutViewSet(viewsets.ModelViewSet):
    """ViewSet for Workout model"""
    queryset = Workout.objects.all()
    serializer_class = WorkoutSerializer
