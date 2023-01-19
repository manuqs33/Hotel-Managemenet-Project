compose = docker-compose
manage = python manage.py

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
	$(manage) shell_plus

