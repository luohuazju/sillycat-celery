from celery import Celery
import time
import settings


echo_celery = Celery("echo_celery", backend=settings.CELERY_BACKEND, broker=settings.CELERY_BROKER)

# echo_celery.conf.beat_scheduler = 'celery.beat:PersistentScheduler'
echo_celery.conf.beat_scheduler = 'celery.beat:MemoryScheduler'

echo_celery.conf.beat_schedule = {
    'scheduled_echo': {
        'task': 'scheduled_echo',
        'schedule': 5.0, # runs in every 5 seconds
        # 'args': (arg1, arg2, ...), Run the function with arguments
    }
}


@echo_celery.task(
    name="scheduled_echo",
    default_retry_delay=300,
    max_retry=1,
    soft_time_limit=30
)
def echo():
    time.sleep(10)
    print("echo task is running and finished!")
