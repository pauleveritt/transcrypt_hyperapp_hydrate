Transcrypt + Hyperapp
=====================

`Transcrypt <http://www.transcrypt.org>`_ is fantastically interesting:
write advanced JavaScript from advanced Python.
`Hyperapp <https://github.com/jorgebucaran/hyperapp>`_ is fantastically
interesting: modern browser applications in a tiny amount of code.

But the JS toolchain? Ugh. My GatsbyJS ``node_modules`` is 500 Mb. Isn't 
there a better way? Python, and Transcrypt, to the rescue. Write your JS in
Python, where it can execute both in a Python web application and later
in the browser. Same code.

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