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

    # Create a Sentinel instance
    sentinel = Sentinel("sentinel://:laproadminpwd@lapro-base-3:26379/2", socket_timeout=0.5, password='laproadminpwd')

    # Discover the master for the specified master name
    master_host, master_port = sentinel.discover_master(master_name)
    print(f"Connected to Redis master: {master_host}:{master_port}")
except Exception as e:
    print(f"Connection failed: {e}")