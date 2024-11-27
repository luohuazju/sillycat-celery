from kombu import Connection
from redis.sentinel import Sentinel


conn = Connection(
    "sentinel://:laproadminpwd@lapro-base-3:26379/2",
    transport_options={'master_name': 'laprocluster'}
)

try:
    conn.connect()
    print("Connection successful!")
    # Extract master name from transport options
    master_name = conn.transport_options.get('master_name')
    if not master_name:
        raise ValueError("Master name is not defined in transport options.")

    # Manually create a Sentinel instance
    sentinel_hosts = conn.transport.get_sentinel_instance().sentinels
    sentinel = Sentinel(sentinel_hosts, socket_timeout=0.5, password="laproadminpwd")

    # Retrieve master node information
    master_host, master_port = sentinel.discover_master(master_name)
    print(f"Connected to Redis master: {master_host}:{master_port}")
except Exception as e:
    print(f"Connection failed: {e}")