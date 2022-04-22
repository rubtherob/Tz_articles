release: python manage.py migrate
release: python manage.py User.objects.create_superuser(email='rubtherobs@gmail.com', password='1')
web: gunicorn TZ.wsgi --log-file -