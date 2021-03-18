from api.models import Like
from django.core.management import BaseCommand


class Command(BaseCommand):
    help = "Resets all likes"

    def handle(self, *args, **options):
        likes = Like.objects.all()
        if likes.delete()[0] > 0:
            self.stdout.write("Likes cleared")
        else:
            self.stdout.write("There was no likes")
