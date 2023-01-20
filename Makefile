compose = docker-compose
manage = python manage.py

run:
	python3 manage.py runserver 0.0.0.0:8000

start:
	$(compose) up

stop:
	$(compose) stop

build:
	$(compose) build


# Container shell --------------------------------------------------------------
shell:
	$(manage) shell

shell_plus:
	$(manage) shell_plus --ipython

migrations:
	$(manage) makemigrations

migrate:
	$(manage) migrate

superuser:
	$(manage) createsuperuser

