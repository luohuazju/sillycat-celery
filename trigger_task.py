from celery_task_ai import ai
#from celery_task_ai import ai_celery

# ai.delay()
ai.apply_async(kwargs={},
               transport_options={'master_name': 'laprocluster'},
               result_backend_transport_options={'master_name': 'laprocluster'})
#ai_celery.send_task(
#    'ai_task',
#    broker_transport_options={'master_name': 'laprocluster'}
#)
# ai.apply_async(kwargs={}, transport_options={'master_name': 'laprocluster'})