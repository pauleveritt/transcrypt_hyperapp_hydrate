==============
Hello HyperApp
==============

Lots of choices for JavaScript frontend frameworks, with React leading
the way. But most of those choices end up meaning a *ginormous* toolchain
of ever-changing, ever-breaking tools to transpile the universe.

HyperApp is the impossibly-small, yet feature-rich JS framework. Small as
in, under 1 KB. Small enough to not actually need minification and
bundling...and in browsers which support
`ES Modules <https://caniuse.com/#feat=es6-module>`_ you still get
import semantics without tools like webpack.

Let's wire up our counter.

.. literalinclude:: counter.js

.. note::

    Because we aren't bundling, we get ``hyperapp`` and ``hyperappHtml``
    from the ``window`` object.

What's in this simple counter?

- A section at the top that is the moral-equivalent of ES6 imports

- The initial state of the counter

- Two *actions*, which are arrow functions which HyperApp calls, providing
  the state

- The *view*, which is usually JSX, but we are doing using the HyperApp
  ``html`` helper package. We don't want JSX because we don't want a
  JavaScript toolchain to have to process it into JS. We have another
  reason, which we'll reveal in the next section.

- The actual ``app`` which wires the pieces together and taks over the
  ``counter`` node in the markup

As a recap:

- On the first load, Bottle runs the template and generates -- server-side
  in Python -- the initial HTML

- JavaScript then kicks in and "hydrates" the existing DOM element,
  rendering the view into it...keeping the existing nodes which are the same,
  replacing changed ones, and adding new ones. This is the mythical "VDOM"
  that you may have heard of.

To emphasize: we are doing SSR, but with Python, not a NodeJS framework.