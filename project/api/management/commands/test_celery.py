from django.core.management import BaseCommand

SCHED = 0.0


class Command(BaseCommand):
    help = "Test if Celery working well"

    def handle(self, *args, **options):
        self.stdout.write("Celery is working")
