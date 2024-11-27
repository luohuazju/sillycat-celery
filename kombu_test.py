from kombu import Connection


conn = Connection(
    "sentinel://:laproadminpwd@lapro-base-3:26379/2",
    transport_options={'master_name': 'laprocluster'}
)

try:
    conn.connect()
    print("Connection successful!")
    redis_connection = conn.transport.driver_redis()
    sentinel_connection = redis_connection.connection_pool.connection_kwargs.get('connection_pool', None)
    if sentinel_connection and hasattr(sentinel_connection, 'sentinel'):
        master = sentinel_connection.sentinel.master_for('laprocluster').connection_pool.connection_kwargs
        print(f"Connected to Redis master: {master['host']}:{master['port']}")
except Exception as e:
    print(f"Connection failed: {e}")