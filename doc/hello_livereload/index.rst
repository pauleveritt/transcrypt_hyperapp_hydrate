================
Hello LiveReload
================

Let's get some bits on the screen. In this step we're going to make a
small Bottle application which returns an HTML template and the
two script tags to load our HyperApp files.

LiveReload
==========

Make a file ``run_server.py`` with the following:

.. literalinclude:: run_server.py

This is a simple Bottle app with two routes:

- ``/`` uses a Bottle template at ``index.tpl`` to dynamically render
  a response

- Everything else is served as static files from the root directory.

Template
========

Now make ``index.tpl``:

.. literalinclude:: index.tpl
    :language: html

This template is passed in the "state" of the application. It inserts the
``count`` value, as well as includes ``script`` and ``link`` tags for
the static assets.

As this shows, when the browser makes a request to the URL, you get
"server-side rendering": the current value of ``count`` is inserted, as
well as the two buttons which will later be made dynamic.

JS
==

As a placeholder for the next step, create ``counter.js``:

.. literalinclude:: counter.js

CSS
===

Not much in ``index.css``:

.. literalinclude:: index.css

Running
=======

With that in place, let's run the server:

.. code-block:: bash

    $ python ./run_server.py

Open ``http://127.0.0.1:5500/`` in a browser, preferably with the dev
console open. You get the first render.

Now try editing the ``run_server.py`` and changing the initial count. The
application restarts and you see the new value.

Now edit ``index.tpl`` and ``index.css``. The changes update much faster,
as the Python process doesn't restart. Instead, the server tells the
browser to reload.