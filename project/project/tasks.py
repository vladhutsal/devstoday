from celery import shared_task
from django.core.management import call_command

_SCHED = 0.0


@shared_task
def toogle_test_celery():
    call_command("test_celery")


@shared_task
def reset_likes():
    call_command("reset_likes")
