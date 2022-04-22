release: python manage.py superuserstart
release: python manage.py migrate
web: gunicorn TZ.wsgi --log-file -