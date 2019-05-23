help:
	@echo "Usage:"
	@echo "    make help        show this message"
	@echo "    make build       create python package"
	@echo "    make upload      upload package to pypi"
	@echo "    make init        create virtual environment and install dependencies"
	@echo "    make setup       do migrations and collect static files"
	@echo "    make activate    enter virtual environment"
	@echo "    make test        run the test suite"
	@echo "    exit             leave virtual environment"

build:
	python3 setup.py sdist bdist_wheel
	twine check dist/*

upload:
	twine upload dist/*
	rm -dr build/ dist/ *.egg-info

init:
	pip install pipenv
	pipenv install --dev --three

setup:
	cp testproject/settings.py.sample testproject/settings.py
	sed -i -e "s/SECRET_KEY = '.*'/SECRET_KEY = '_'/" testproject/settings.py


activate:
	pipenv shell -c

test:
	pipenv run ./manage.py test
	pipenv run coverage run ./manage.py test

.PHONY: help activate test
