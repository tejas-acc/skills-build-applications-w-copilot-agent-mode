from django.core.management.base import BaseCommand
from octofit_tracker.models import User, Team, Activity, Leaderboard, Workout
from datetime import date

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **kwargs):
        # Clear existing data
        User.objects.all().delete()
        Team.objects.all().delete()
        Activity.objects.all().delete()
        Leaderboard.objects.all().delete()
        Workout.objects.all().delete()

        # Teams
        marvel = Team.objects.create(name='marvel', description='Marvel superheroes')
        dc = Team.objects.create(name='dc', description='DC superheroes')

        # Users
        users = [
            User.objects.create(email='ironman@marvel.com', name='Iron Man', team='marvel'),
            User.objects.create(email='captain@marvel.com', name='Captain America', team='marvel'),
            User.objects.create(email='batman@dc.com', name='Batman', team='dc'),
            User.objects.create(email='superman@dc.com', name='Superman', team='dc'),
        ]

        # Activities
        Activity.objects.create(user='ironman@marvel.com', activity_type='run', duration=30, date=date.today())
        Activity.objects.create(user='captain@marvel.com', activity_type='cycle', duration=45, date=date.today())
        Activity.objects.create(user='batman@dc.com', activity_type='swim', duration=25, date=date.today())
        Activity.objects.create(user='superman@dc.com', activity_type='fly', duration=60, date=date.today())

        # Leaderboard
        Leaderboard.objects.create(user='ironman@marvel.com', team='marvel', points=100)
        Leaderboard.objects.create(user='captain@marvel.com', team='marvel', points=90)
        Leaderboard.objects.create(user='batman@dc.com', team='dc', points=110)
        Leaderboard.objects.create(user='superman@dc.com', team='dc', points=120)

        # Workouts
        Workout.objects.create(name='Pushups', description='Do 20 pushups', difficulty='easy')
        Workout.objects.create(name='Sprints', description='Sprint 100m', difficulty='medium')
        Workout.objects.create(name='Plank', description='Hold plank for 2 minutes', difficulty='hard')

        self.stdout.write(self.style.SUCCESS('octofit_db database populated with test data.'))
