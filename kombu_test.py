from kombu import Connection


conn = Connection(
    "sentinel://:laproadminpwd@lapro-base-3:26379/2",
    transport_options={'master_name': 'laprocluster'}
)

try:
    conn.connect()
    print("Connection successful!")
except Exception as e:
    print(f"Connection failed: {e}")