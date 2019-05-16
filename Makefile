help:
	@echo "Usage:"
	@echo "    make help        show this message"
	@echo "    make build       create python package"
	@echo "    make upload      upload package to pypi"
	@echo "    make setup       create virtual environment and install dependencies"
	@echo "    make activate    enter virtual environment"
	@echo "    make test        run the test suite"
	@echo "    exit             leave virtual environment"

build:
	python3 setup.py sdist bdist_wheel
	twine check dist/*

upload:
	twine check dist/*
	rm -dr build/ dist/ *.egg-info

setup:
	pip install pipenv
	pipenv install --dev --three

activate:
	pipenv shell -c

test:
	pipenv run -- ./manage.py test
	pipenv run -- coverage run ./manage.py test

.PHONY: help activate test
