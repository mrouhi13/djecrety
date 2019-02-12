Usage
============

This is really simple, there is only one command with 3 optional arguments.

Let's go!

* ``djecrety`` command with no argument, generate and display a new secret key:

.. code-block:: text

    $ ./manage.py djecrety

* With ``-s`` argument, save the generated secret key to ``settings.py`` file:

.. code-block:: text

    $ ./manage.py djecrety -s

* With ``-p`` argument, display the generated secret key when saving on file:

.. note::

    ``-p`` argument work when saving the secret key to file.

.. code-block:: text

    $ ./manage.py djecrety -sp

* With ``-d`` argument, specify settings directory name:

.. note::

    By default, we try to detect your project directory and ``settings.py`` file location, if ``settings.py`` file not in default location you can specify the directory.

.. code-block:: text

    $ ./manage.py djecrety -sp
