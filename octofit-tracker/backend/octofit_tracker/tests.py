from django.test import TestCase
from rest_framework.test import APITestCase
from rest_framework import status
from .models import User, Team, Activity, Leaderboard, Workout


class UserModelTestCase(TestCase):
    """Test cases for User model"""
    
    def setUp(self):
        self.user = User.objects.create(
            username='testuser',
            email='test@example.com',
            first_name='Test',
            last_name='User'
        )
    
    def test_user_creation(self):
        self.assertEqual(self.user.username, 'testuser')
        self.assertEqual(self.user.email, 'test@example.com')


class TeamModelTestCase(TestCase):
    """Test cases for Team model"""
    
    def setUp(self):
        self.team = Team.objects.create(
            name='Test Team',
            description='A test team'
        )
    
    def test_team_creation(self):
        self.assertEqual(self.team.name, 'Test Team')


class ActivityModelTestCase(TestCase):
    """Test cases for Activity model"""
    
    def setUp(self):
        self.activity = Activity.objects.create(
            user_id='testuser',
            activity_type='running',
            duration_minutes=30,
            calories_burned=250.0,
            distance_km=5.0
        )
    
    def test_activity_creation(self):
        self.assertEqual(self.activity.activity_type, 'running')
        self.assertEqual(self.activity.duration_minutes, 30)


class UserAPITestCase(APITestCase):
    """Test cases for User API endpoints"""
    
    def setUp(self):
        self.user = User.objects.create(
            username='apiuser',
            email='api@example.com'
        )
    
    def test_list_users(self):
        url = '/api/users/'
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class TeamAPITestCase(APITestCase):
    """Test cases for Team API endpoints"""
    
    def setUp(self):
        self.team = Team.objects.create(
            name='API Test Team',
            description='Test team for API'
        )
    
    def test_list_teams(self):
        url = '/api/teams/'
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
