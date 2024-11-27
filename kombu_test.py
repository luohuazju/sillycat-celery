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
    print(master_name)
except Exception as e:
    print(f"Connection failed: {e}")