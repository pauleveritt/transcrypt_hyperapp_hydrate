from bottle import route, default_app, static_file
from livereload import Server


@route('/')
def index():
    return f'<h1>Demo</h1><p>Hellos</p>'


# @route('/static/<filepath:path>')
# def server_static(filepath):
#     return static_file(filepath, root='hydrate')


def transpile():
    print('Running transcrypt')


if __name__ == '__main__':
    app = default_app()
    server = Server(app)
    server.watch('hydrate/demo.py', transpile)
    server.watch('hydrate/index.html')
    server.serve()
