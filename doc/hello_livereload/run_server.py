import bottle
from bottle import route, default_app, static_file
from bottle import template
from livereload import Server

bottle.debug(True)


@route('/')
def index():
    return template('index', state=dict(count=0))


@route('/<filepath:path>')
def server_static(filepath):
    return static_file(filepath, root='.')


if __name__ == '__main__':
    app = default_app()
    server = Server(app)
    server.watch('index.css')
    server.watch('counter.js')
    server.watch('index.tpl', ignore=False)
    server.serve()
