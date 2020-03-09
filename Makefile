help:
	@echo "Usage:"
	@echo "    make help        show this message"
	@echo "    make build       create python package"
	@echo "    make init        create virtual environment and install dependencies"
	@echo "    make setup       do migrations and collect static files"
	@echo "    make test        run the test suite"
	@echo "    exit             leave virtual environment"

build:
	python3 setup.py sdist bdist_wheel
	twine check dist/*

init:
	pip install pipenv
	pipenv install --dev --three

setup:
	cp testproject/settings.py.sample testproject/settings.py

test:
	pipenv run coverage erase
	pipenv run ./manage.py test
	pipenv run coverage run ./manage.py test
	pipenv run coverage report

.PHONY: help activate test
