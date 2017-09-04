from celery import Celery
app = Celery('demo1')
app.config_from_object('celery_time.celeryconfig')
