from celery import shared_task
from celery.schedules import crontab
from django.core.management import call_command


class SchedMeta(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance
        return cls._instances[cls]


class Sched(metaclass=SchedMeta):
    def __init__(self, default=crontab(minute=0, hour=0)):
        self._default = default
        self.curr_t = default
    
    def toogle_timer(self):
        timer_is_cron = self.curr_t == self._default
        self.curr_t = 2.0 if timer_is_cron else self._default

        if timer_is_cron:
            return "daily at midnight"
        return "every two seconds"

    
    def get_timer(self):
        return self.curr_t


_SCHED = Sched()


@shared_task
def toogle_test_celery():
    call_command("test_celery")


@shared_task
def reset_likes():
    call_command("reset_likes")
