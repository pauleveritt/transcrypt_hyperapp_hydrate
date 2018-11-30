=====
Setup
=====

We need to do the normal Python dance: make a virtual environment and
install our dependencies. We also need to download the two files from
HyperApp.

We want to show going an extra step and get the packages for a development
environment that matches some of the webpack-devserver auto-build/reload.

Virtual Environment
===================

This one is obvious:

.. code-block:: bash

    $ python3 -m venv .env
    $ .env/bin/pip install --upgrade pip setuptools

Dependencies
============

We need Transcrypt, obviously. We're also going to use Bottle connected to
the Python ``livereload`` package to watch for changes and reload the
browser:

.. code-block::bash

    $ .env/bin/pip install transcrypt bottle livereload==2.5.1

.. note::

    We're picking a specific livereload version to avoid a bug.

Let's also get our two JS files, HyperApp itself and a HyperApp HTML
helper package (as an alternative to JSX):

.. code-block:: bash

    $ wget https://unpkg.com/hyperapp@1.2.9/dist/hyperapp.js
    $ wget https://unpkg.com/@hyperapp/html@1.1.1/dist/hyperappHtml.js

