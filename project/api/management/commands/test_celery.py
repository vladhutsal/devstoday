from django.core.management import BaseCommand


class Command(BaseCommand):
    help = "Test if Celery working well"

    def handle(self, *args, **options):
        self.stdout.write("Celery is working")
