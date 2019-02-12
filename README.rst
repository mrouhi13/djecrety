=====
Djecrety
=====

Djecrety is a simple Django app to work with "settings.py" file such as import/export sensitive values, generate a new secret key, add new parameters and update the existing. It also has a web-based tool for generating Django secret key.

Detailed documentation is in the "docs" directory.

Getting started
===============

Available Commands
-------------------

* djecrety

Supported Python versions
-------------------------

* Python 3.4
* Python 3.5
* Python 3.6

Supported Django versions
-------------------------

* Django 1.11
* Django 2.0
* Django 2.1

Installation
------------

.. code-block:: bash

    $ pip install -U djecrety

Configuration
-------------

Configure ``INSTALLED_APPS``:

.. code-block:: python

    INSTALLED_APPS = (
        (...),
        'djecrety',
        (...),
    )

Usage
============

This is really simple, there is only one command with 3 optional arguments.
Let's go!

`djecrety` command with no argument, generate and display a new secret key:

.. code-block:: text

    $ ./manage.py dejcrety

With `-s` argument, save the generated secret key to `settings.py` file:

.. code-block:: text

    $ ./manage.py dejcrety -s

With `-p` argument, display the generated secret key when saving on file:

.. note::

    `-p` argument work when saving the secret key to file.

.. code-block:: text

    $ ./manage.py dejcrety -sp

With `-d` argument, specify settings directory name:

.. note::

    By default, we try to detect your project directory and `settings.py` file location, if `settings.py` file not in default location you can specify the directory.

.. code-block:: text

    $ ./manage.py dejcrety -sp
