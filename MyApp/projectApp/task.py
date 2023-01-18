from celery import shared_task
from time import sleep

@shared_task
def Main_task(duration):
    sleep(duration)
    return None