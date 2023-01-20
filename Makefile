compose = docker-compose
manage = python manage.py

start:
	$(compose) up

stop:
	$(compose) stop

build:
	$(compose) build


# Shell and Django commands--------------------------------------------------------------
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

