from celery import Celery
import time
import settings


ai_celery = Celery("ai_celery", backend=settings.CELERY_BACKEND, broker=settings.CELERY_BROKER)

print("Broker URL:", settings.CELERY_BROKER)
print("Backend URL:", settings.CELERY_BACKEND)
print("transport options:", settings.CELERY_BROKER_TRANSPORT_OPTIONS)

ai_celery.conf.update(
    broker_url=settings.CELERY_BROKER,  # Redis broker URL
    result_backend=settings.CELERY_BACKEND,  # Redis result backend
    broker_transport_options={
        'master_name': 'laprocluster',  # Redis master name
    }
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
