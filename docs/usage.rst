Usage
============

This is really simple, there is only one command with 3 optional arguments.

Let's go!

* ``djecrety`` command with no argument, generate and display a new secret key:

.. code-block:: text

    $ ./manage.py djecrety

* With ``-s`` argument, save the generated secret key to ``settings.py``:

.. code-block:: text

    $ ./manage.py djecrety -s

* With ``-p`` argument, display the generated secret key while saving to the file:

.. note::

    ``-p`` argument work with ``-s`` argument.

.. code-block:: text

    $ ./manage.py djecrety -sp

* With ``-d`` argument, specify settings directory name:

.. note::

    By default, Djecrety try to detect your project directory and ``settings.py`` location, if ``settings.py`` not in default location you can specify the directory name.

.. code-block:: text

    $ ./manage.py djecrety -d testproject
