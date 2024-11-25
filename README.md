# sillycat-celery
python  celery redis as broker, flower to monitor

```
celery -A celery_task_ai worker --loglevel=DEBUG

celery -A celery_task_echo worker --loglevel=DEBUG
```

Or start the ai worker
```
pm2 start pm2-celery-worker.config.js 
```

We can directly deploy the tasks

```
from celery_task_ai import ai
from celery_task_echo import echo


ai.delay()
echo.delay()
```

Run the task
```
python trigger_task.py
```

Command to start Beat

```
celery -A celery_task_echo beat --loglevel=DEBUG
```

Command to start a Redis
```
docker run -p 6379:6379 redis:alpine
```

Command to restart the monitor
```
celery --broker=redis://127.0.0.1:6379/2 flower  
```
