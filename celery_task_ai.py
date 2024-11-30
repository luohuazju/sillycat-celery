from celery import Celery
import time
import settings


ai_celery = Celery(
    "ai_celery",
    backend=settings.CELERY_BACKEND,
    broker=settings.CELERY_BROKER,
    broker_transport_options={'master_name': 'laprocluster'},
    result_backend_transport_options={'master_name': 'laprocluster'}
)

@ai_celery.task(
    name="ai_task",
    default_retry_delay=300,
    max_retry=1,
    soft_time_limit=30
)
def ai():
    time.sleep(10)
    print("AI task is running and finished!")


# Trigger the task conditionally
if __name__ == "__main__":
    print("Broker Transport Options trigger:", ai_celery.conf.broker_transport_options)
    print(f"Backend Transport Options: {ai_celery.conf.result_backend_transport_options}")
    result = ai.delay()  # Trigger the task
    print(f"Task has been sent. Task ID: {result.id}")
