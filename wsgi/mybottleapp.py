from bottle import route, default_app, request, response, template


@route('/name/<name>')
def nameindex(name='Stranger'):
    return '<strong>Hello, %s!</strong>' % name


@route('/')
def index():
    return '<strong>Hello World!</strong>'


@route('/pdf')
def pdf():
    url = request.query.url
    return url

# This must be added in order to do correct path lookups for the views
import os
from bottle import TEMPLATE_PATH

TEMPLATE_PATH.append(os.path.join(os.environ['OPENSHIFT_REPO_DIR'], 'wsgi/views/'))

application = default_app()
