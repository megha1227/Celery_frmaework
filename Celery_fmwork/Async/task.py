import time
from celery import Celery


celery = Celery('task',broker='redis://localhost/0',backend='redis://localhost/0')



@celery.task
def task():
    print("Starting the task")
    print("Simulating a delay")
    time.sleep(10)
    print("task got completed")