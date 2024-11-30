from celery_task_ai import ai
#from celery_task_ai import ai_celery


result = ai.delay()  # Trigger the task
print(f"Task has been sent. Task ID: {result.id}")
#ai_celery.send_task(
#    'ai_task',
#    broker_transport_options={'master_name': 'laprocluster'}
#)
