from bottle import route, default_app, request, response
import pdfkit
import unicodedata


@route('/')
def index():
    return '<strong>Hello World!</strong>'


@route('/pdf')
def pdf():
    url = unicodedata.normalize('NFKD', request.query.url).encode('ascii', 'ignore')

    response.content_type = 'application/pdf; charset=UTF-8'
    response.headers['Content-Disposition'] = 'attachment; filename="test.pdf"'

    generated_pdf = pdfkit.from_url(url, False)
    return generated_pdf


# This must be added in order to do correct path lookups for the views
import os
from bottle import TEMPLATE_PATH

TEMPLATE_PATH.append(os.path.join(os.environ['OPENSHIFT_REPO_DIR'], 'wsgi/views/'))

application = default_app()
