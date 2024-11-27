from kombu import Connection, Exchange, Queue


# Kombu Connection
kombu_conn = Connection(
    "sentinel://:laproadminpwd@lapro-base-3:26379/2",
    transport_options={'master_name': 'laprocluster'}
)

# Define Exchange and Queue
exchange = Exchange("celery", type="direct")
queue = Queue("celery", exchange, routing_key="celery")

# Produce Task Manually
with kombu_conn.Producer() as producer:
    producer.publish(
        {"id": "task_id", "task": "ai_task", "args": [], "kwargs": {}},
        exchange=exchange,
        routing_key="celery",
        declare=[queue],
        serializer="json",
    )

print("Task sent manually via Kombu!")
