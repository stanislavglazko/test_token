install:
	@poetry install

lint:
	@poetry run flake8

selfcheck:
	poetry check

check: selfcheck lint

build: check
	@poetry build

run:
	poetry run python3 manage.py runserver

test:
	poetry run coverage run manage.py test
	poetry run coverage xml

.PHONY: install test lint selfcheck check build
