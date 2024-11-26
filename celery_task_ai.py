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

ai_celery.conf.update(
    broker_url=settings.CELERY_BROKER,  # Redis broker URL
    result_backend=settings.CELERY_BACKEND,  # Redis result backend
    broker_transport_options={
        'master_name': 'laprocluster',  # Redis master name
    },
    result_backend_transport_options={
        'master_name': 'laprocluster'
    }
)

# Print configuration to verify
print("Current Celery Configuration:")
print(f"Broker URL: {ai_celery.conf.broker_url}")
print(f"Result Backend: {ai_celery.conf.result_backend}")
print(f"Broker Transport Options: {ai_celery.conf.broker_transport_options}")
print(f"Backend Transport Options: {ai_celery.conf.result_backend_transport_options}")

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
    ai.apply_async(kwargs={}, transport_options={'master_name': 'laprocluster'})
    #result = ai.delay()  # Trigger the task
    #print(f"Task has been sent. Task ID: {result.id}")
