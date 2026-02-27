"""octofit_tracker URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
import os
from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .views import (
    api_root as original_api_root,
    UserViewSet,
    TeamViewSet,
    ActivityViewSet,
    LeaderboardViewSet,
    WorkoutViewSet,
)

# Create router and register viewsets
router = DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'teams', TeamViewSet)
router.register(r'activities', ActivityViewSet)
router.register(r'leaderboard', LeaderboardViewSet)
router.register(r'workouts', WorkoutViewSet)

# Determine base URL based on environment
codespace_name = os.environ.get('CODESPACE_NAME')
if codespace_name:
    BASE_URL = f"https://{codespace_name}-8000.app.github.dev"
else:
    BASE_URL = "http://localhost:8000"


@api_view(['GET'])
def api_root(request):
    """API root endpoint with Codespace-aware URLs"""
    return Response({
        'message': 'Welcome to OctoFit Tracker API',
        'version': '1.0.0',
        'endpoints': {
            'users': f'{BASE_URL}/api/users/',
            'teams': f'{BASE_URL}/api/teams/',
            'activities': f'{BASE_URL}/api/activities/',
            'leaderboard': f'{BASE_URL}/api/leaderboard/',
            'workouts': f'{BASE_URL}/api/workouts/',
        }
    })


urlpatterns = [
    path('', api_root, name='api-root'),
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
]
