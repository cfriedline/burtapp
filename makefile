D=python manage.py
WSGI=uwsgi.ini

update_db:
	$D makemigrations
	$D migrate

runserver:
	$D runserver

static:
	$D collectstatic

touch:
	touch $(WSGI)

nginx:
	sudo cp django.nginx /etc/nginx/sites-available/django
