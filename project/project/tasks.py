from celery import shared_task
from django.core.management import call_command

@shared_task
def reset_likes():
    call_command("reset_likes")
