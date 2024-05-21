# sillycat-celery
python  celery redis as broker, flower to monitor

```
celery -A ai_celery worker --loglevel=INFO

celery -A echo_celery worker --loglevel=INFO
```

We can directly deploy the tasks

```
from celery_task_ai import ai
from celery_task_echo import echo


ai.delay()
echo.delay()
```

Command to start Beat

```
celery -A echo_celery beat --loglevel=INFO
```

Command to start a Redis
```
docker run -p 6379:6379 redis:alpine
```