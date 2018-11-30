================
Hello Transcrypt
================

This step is gonna get freaky.

Perhaps you noticed that we wrote the counter in JS. Perhaps you noticed
that there will therefore be a duplication in implementation logic:
Python for the first render and JavaScript for once it is hydrated.

Let's write the counter once, in Python, and have Transcrypt generate
the JS for HyperApp.

Counter, In Python
==================

Make a file called ``counter.py``:

.. literalinclude:: counter.py

This is a Python file that will be run through Transcrypt to generate the
moral equivalent of ``counter.js`` which we just saw. If you use a smart
editor, you'll see red squigglies complaining that ``window`` and
``document`` are undefined.

And that's true. Those are symbols which don't exist in Python. They
spring into existence when run in JavaScript.

.. note::

    Need to find a way to teach the editor that those symbols can
    exist and give them a structure.

In the first line, you see a Python import of ``hyperappHtml``. What's that?
The ``hyperapp/html`` "package" is really a single, simple file. This
tutorial just converted it to Python, to allow us to work towards a single
"template" which works both on initial render (in Python) and browser-side
(in JS).

And here's that file.

HTML Helper
===========

Create ``hyperappHtml.py`` with the following:

.. literalinclude:: hyperappHtml.py

As you can see, this is just a proof-of-concept:

- It doesn't include all the tags

- It can't be used 100% in Python, because it still needs the ``h`` function
  from HyperApp (only 60 or so lines, but dense in concepts)

Still, it allows us to use Python tooling (e.g. type hinting) when writing
our views, rather than rely on some alien symbol representing a JavaScript
function.

Loading the Generated JS
========================

Transcrypt is going to read our Python and generate JS. We need to load
that generated JS. Transcrypt generated ESM-friendly JS, so we can do an
import. Change ``index.tpl`` to (a) remove loading ``hyperHtml.js``,
(b) remove loading ``counter.js``, and (c) add the new ``<script``:

.. literalinclude:: index.tpl

Run Transcrypt
==============

Now it's time to get Transcrypt to do its magic. Let's have ``run_server.py``
handle it, so we can run it any time ``counter.py`` changes. Even better,
the browser will reload with our changes.

.. literalinclude:: run_server.py

In the previous step, the initial-rendering (in Python) used a different
state than the hydrated count, which was in JS. Now that the counter is in
Python, we can import the initial value and hand it to the template.

Future: One Template
====================

This is all a little freaky. It's hard to remember some times which
side of the fence is governing which of the executions (initial in Python,
later in JS.)

Of course, it can get a lot freakier. For example, we still have two
templates:

- The ``index.tpl`` Bottle template

- The ``hyperapp/html`` (converted to Python) in the HyperApp view

Wouldn't it be great if there was just one template? That way the initial
render could use the same template that was used later.

A full-port of ``hyperapp/html`` to Python is half the equation. The other
is harder: porting the "h" function is also needed. It's short but
complicated. Some of the complexity could go, as a diff isn't needed: this
is the first render.

