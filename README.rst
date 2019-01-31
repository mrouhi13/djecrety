=====
Djecrety
=====

Djecrety is a simple Django app to work with "settings.py" file such as import/export sensitive values, generate a new secret key, add new parameters and update the existing. It also has a web-based tool for generating Django secret key.

Detailed documentation is in the "docs" directory.

Quickstart
-----------

1. Add "djecrety" to your INSTALLED_APPS setting like this:

    INSTALLED_APPS = [
        ...
        'djecrety',
    ]

2. Run `python manage.py djecrety help` to see available commands.
