from django.test import TestCase
from .models import User, Team, Activity, Workout, Leaderboard

class ModelTests(TestCase):
    def setUp(self):
        self.team = Team.objects.create(name='Marvel', description='Marvel superheroes')
        self.user = User.objects.create(name='Tony Stark', email='tony@stark.com', team=self.team)
        self.workout = Workout.objects.create(name='Super Strength', description='Strength workout')
        self.workout.suggested_for.add(self.team)
        self.activity = Activity.objects.create(user=self.user, activity_type='Running', duration=30, date='2023-01-01')
        self.leaderboard = Leaderboard.objects.create(team=self.team, total_points=100)

    def test_user_email_unique(self):
        with self.assertRaises(Exception):
            User.objects.create(name='Duplicate', email='tony@stark.com', team=self.team)

    def test_team_str(self):
        self.assertEqual(str(self.team), 'Marvel')

    def test_user_str(self):
        self.assertEqual(str(self.user), 'tony@stark.com')

    def test_activity_str(self):
        self.assertIn('tony@stark.com', str(self.activity))

    def test_workout_str(self):
        self.assertEqual(str(self.workout), 'Super Strength')

    def test_leaderboard_str(self):
        self.assertIn('Marvel', str(self.leaderboard))
