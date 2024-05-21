from celery import Celery
import time
import settings


ai_celery = Celery("ai_celery", backend=settings.CELERY_BACKEND, broker=settings.CELERY_BROKER)


@ai_celery.task(
    name="ai_task",
    default_retry_delay=300,
    max_retry=1,
    soft_time_limit=30
)
def ai():
    time.sleep(10)
    print("AI task is running and finished!")
