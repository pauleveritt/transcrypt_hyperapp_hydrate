import bottle
from bottle import route, default_app, static_file
from bottle import template
from livereload import Server, shell

from hydrate.demo import state

# TODO Instead of forking and running Python, extract
#   stuff from transcrypt.__main__.main
transpile = '../env/bin/transcrypt -b -m -n demo.py'

bottle.debug(True)


@route('/')
def index():
    return template('hydrate/index', state=state)


@route('/<filepath:path>')
def server_static(filepath):
    return static_file(filepath, root='hydrate')


if __name__ == '__main__':
    app = default_app()
    server = Server(app)
    server.watch('hydrate/demo.py', shell(transpile, cwd='hydrate'))
    server.watch('hydrate/__target__/*', delay=2)
    server.watch('hydrate/demo.css')
    server.watch('hydrate/index.tpl', ignore=False)
    server.serve(root='hydrate')
