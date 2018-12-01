Transcrypt + HyperApp
=====================

`Transcrypt <http://www.transcrypt.org>`_ is fantastically interesting:
write advanced JavaScript from advanced Python.
`HyperApp <https://github.com/jorgebucaran/hyperapp>`_ is fantastically
interesting: modern browser applications in a tiny amount of code.

Let's do an example, in tutorial format, of explaining these two,
individually and in combination. Let's then explore some further topics:

- Server-Side-Rendering(SSR), where the initial page's HTML is generated
  and delivered, then replaced with client-side rendering if JS is supported
  (aka "hydration")

Other topics in the future:

- Transcrypt's static type analysis

- Client-side routing, where links between pages are intercepted and
  handled with a JS router

- Doing server-side "templating" and client-side "templating" with the
  same code

- Link pre-fetching

- Offline-first

.. toctree::
    :maxdepth: 2
    :caption: Contents:

    setup
    hello_livereload/index
    hello_hyperapp/index
    hello_transcrypt/index
    next