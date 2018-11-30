import bottle
from bottle import route, default_app, static_file
from bottle import template
from livereload import Server, shell

from counter import state

bottle.debug(True)

# TODO Instead of forking and running Python, extract
#   stuff from transcrypt.__main__.main
transpile = 'env/bin/transcrypt -b -m -n counter.py'


@route('/')
def index():
    return template('index', state=state)


@route('/<filepath:path>')
def server_static(filepath):
    return static_file(filepath, root='.')


if __name__ == '__main__':
    app = default_app()
    server = Server(app)
    server.watch('counter.py', shell(transpile))
    server.watch('hydrate/__target__/*', delay=2)
    server.watch('index.css')
    server.watch('counter.js')
    server.watch('index.tpl', ignore=False)
    server.serve()
