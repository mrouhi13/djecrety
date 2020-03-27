help:
	@echo "Usage:"
	@echo "    make help        show this message"
	@echo "    make build       create python package"
	@echo "    make init        create virtual environment and install dependencies"
	@echo "    make activate    enter virtual environment"
	@echo "    make test        run the test suite"
	@echo "    exit             leave virtual environment"

build:
	python3 setup.py sdist bdist_wheel
	twine check dist/*

init:
	pip install --upgrade pip
	pip install pipenv
	pipenv install --dev --three

activate:
	pipenv shell

test:
	tox -v

.PHONY: help activate test
