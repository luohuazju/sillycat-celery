# config.py
broker_url = 'sentinel://:laproadminpwd@lapro-base-3:26379/2'
broker_transport_options = {'master_name': 'laprocluster'}
result_backend_transport_options={'master_name': 'laprocluster'}