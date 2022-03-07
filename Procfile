release: python manage.py migrate
web: gunicorn korea.wsgi --log-file=-
worker: celery --app korea worker -l info