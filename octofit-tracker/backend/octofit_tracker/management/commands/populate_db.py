from django.core.management.base import BaseCommand
from octofit_tracker.models import User, Team, Activity, Workout, Leaderboard
from django.utils import timezone

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **kwargs):
        self.stdout.write(self.style.WARNING('Deleting old data...'))
        Activity.objects.all().delete()
        User.objects.all().delete()
        Team.objects.all().delete()
        Workout.objects.all().delete()
        Leaderboard.objects.all().delete()

        self.stdout.write(self.style.SUCCESS('Creating teams...'))
        marvel = Team.objects.create(name='Marvel', description='Marvel superheroes')
        dc = Team.objects.create(name='DC', description='DC superheroes')

        self.stdout.write(self.style.SUCCESS('Creating users...'))
        tony = User.objects.create(name='Tony Stark', email='tony@stark.com', team=marvel)
        steve = User.objects.create(name='Steve Rogers', email='steve@marvel.com', team=marvel)
        bruce = User.objects.create(name='Bruce Wayne', email='bruce@dc.com', team=dc)
        clark = User.objects.create(name='Clark Kent', email='clark@dc.com', team=dc)

        self.stdout.write(self.style.SUCCESS('Creating workouts...'))
        workout1 = Workout.objects.create(name='Super Strength', description='Strength workout')
        workout2 = Workout.objects.create(name='Flight Training', description='Flight workout')
        workout1.suggested_for.add(marvel, dc)
        workout2.suggested_for.add(dc)

        self.stdout.write(self.style.SUCCESS('Creating activities...'))
        Activity.objects.create(user=tony, activity_type='Running', duration=30, date=timezone.now())
        Activity.objects.create(user=steve, activity_type='Cycling', duration=45, date=timezone.now())
        Activity.objects.create(user=bruce, activity_type='Martial Arts', duration=60, date=timezone.now())
        Activity.objects.create(user=clark, activity_type='Flying', duration=120, date=timezone.now())

        self.stdout.write(self.style.SUCCESS('Creating leaderboards...'))
        Leaderboard.objects.create(team=marvel, total_points=175)
        Leaderboard.objects.create(team=dc, total_points=180)

        self.stdout.write(self.style.SUCCESS('Database populated with test data!'))
