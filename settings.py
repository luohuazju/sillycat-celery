import os
from dotenv import load_dotenv

load_dotenv()

CELERY_BACKEND = os.getenv('CELERY_BACKEND')
CELERY_BROKER = os.getenv('CELERY_BROKER')
CELERY_BEAT = os.getenv('CELERY_BEAT')
CELERY_BROKER_TRANSPORT_OPTIONS = {'master_name':'laprocluster'}
