from django.core.management.base import BaseCommand
from octofit_tracker.models import User, Team, Activity, Leaderboard, Workout
from django.utils import timezone
from datetime import timedelta
import random


class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **options):
        # Clear existing data using Django ORM
        self.stdout.write("Clearing existing data...")
        User.objects.all().delete()
        Team.objects.all().delete()
        Activity.objects.all().delete()
        Leaderboard.objects.all().delete()
        Workout.objects.all().delete()

        # Create teams
        self.stdout.write("Creating teams...")
        team_marvel = Team.objects.create(
            name='Team Marvel',
            description='Marvel superheroes team'
        )
        team_dc = Team.objects.create(
            name='Team DC',
            description='DC superheroes team'
        )

        # Create users - Marvel superheroes
        self.stdout.write("Creating users...")
        marvel_heroes = [
            ('spider_man', 'Peter Parker', 'peter@marvel.com'),
            ('iron_man', 'Tony Stark', 'tony@marvel.com'),
            ('captain_america', 'Steve Rogers', 'steve@marvel.com'),
            ('thor', 'Thor Odinson', 'thor@marvel.com'),
            ('black_widow', 'Natasha Romanoff', 'natasha@marvel.com'),
        ]

        dc_heroes = [
            ('batman', 'Bruce Wayne', 'bruce@dc.com'),
            ('superman', 'Clark Kent', 'clark@dc.com'),
            ('wonder_woman', 'Diana Prince', 'diana@dc.com'),
            ('flash', 'Barry Allen', 'barry@dc.com'),
            ('green_lantern', 'Hal Jordan', 'hal@dc.com'),
        ]

        users_marvel = []
        users_dc = []

        for username, name, email in marvel_heroes:
            user = User.objects.create(
                username=username,
                email=email,
                first_name=name.split()[0],
                last_name=name.split()[1],
                is_active=True
            )
            users_marvel.append(user)

        for username, name, email in dc_heroes:
            user = User.objects.create(
                username=username,
                email=email,
                first_name=name.split()[0],
                last_name=name.split()[1],
                is_active=True
            )
            users_dc.append(user)

        # Update team members
        team_marvel.members = [user.id for user in users_marvel]
        team_marvel.save()
        team_dc.members = [user.id for user in users_dc]
        team_dc.save()

        # Create activities
        self.stdout.write("Creating activities...")
        activity_types = ['running', 'cycling', 'swimming', 'weightlifting', 'yoga']
        all_users = users_marvel + users_dc

        for user in all_users:
            for _ in range(random.randint(3, 10)):
                activity_type = random.choice(activity_types)
                duration = random.randint(20, 120)
                calories = random.uniform(100, 600)
                distance = random.uniform(2, 20) if activity_type in ['running', 'cycling'] else None

                Activity.objects.create(
                    user_id=user.username,
                    activity_type=activity_type,
                    duration_minutes=duration,
                    calories_burned=calories,
                    distance_km=distance,
                    created_at=timezone.now() - timedelta(days=random.randint(0, 30))
                )

        # Create workouts
        self.stdout.write("Creating workouts...")
        workouts_data = [
            {
                'name': 'Basic Running Routine',
                'description': 'A beginner-friendly running routine for daily fitness',
                'difficulty': 'beginner',
                'duration_minutes': 30,
                'exercises': ['5-minute warmup', '20 minutes steady running', '5-minute cooldown']
            },
            {
                'name': 'Intermediate HIIT',
                'description': 'High-intensity interval training for intermediate level',
                'difficulty': 'intermediate',
                'duration_minutes': 45,
                'exercises': ['10-minute warmup', '30 minutes HIIT', '5-minute cooldown']
            },
            {
                'name': 'Advanced Crossfit',
                'description': 'Advanced crossfit workout routine',
                'difficulty': 'advanced',
                'duration_minutes': 60,
                'exercises': ['5-minute warmup', '50 minutes crossfit exercises', '5-minute cooldown']
            },
            {
                'name': 'Yoga Flexibility',
                'description': 'Yoga for flexibility and relaxation',
                'difficulty': 'beginner',
                'duration_minutes': 45,
                'exercises': ['Warm-up stretches', 'Standing poses', 'Floor poses', 'Cool-down']
            },
            {
                'name': 'Swimming Endurance',
                'description': 'Swimming routine to build endurance',
                'difficulty': 'intermediate',
                'duration_minutes': 50,
                'exercises': ['Warm-up laps', 'Distance swimming', 'Sprint intervals', 'Cool-down laps']
            },
        ]

        for workout_data in workouts_data:
            Workout.objects.create(**workout_data)

        # Create leaderboard entries
        self.stdout.write("Creating leaderboard entries...")
        rank = 1
        for user in sorted(all_users, key=lambda u: u.username):
            activities = Activity.objects.filter(user_id=user.username)
            total_activities = activities.count()
            total_duration = sum(a.duration_minutes for a in activities)
            total_calories = sum(a.calories_burned for a in activities)

            team = team_marvel if user in users_marvel else team_dc

            Leaderboard.objects.create(
                user_id=user.id,
                username=user.username,
                team_id=team.id,
                total_activities=total_activities,
                total_duration_minutes=total_duration,
                total_calories_burned=total_calories,
                rank=rank
            )
            rank += 1

        self.stdout.write(self.style.SUCCESS('Successfully populated the database with test data'))
