from bottle import route, default_app, request, response, template
from io import BytesIO
import requests
from xhtml2pdf import pisa


@route('/')
def index():
    return '<strong>Hello World!</strong>'


@route('/pdf')
def pdf():
    url = request.query.url
    r = requests.get(url)
    pdf_buffer = BytesIO()

    response.content_type = 'application/pdf; charset=UTF-8'
    response.headers['Content-Disposition'] = 'attachment; filename="test.pdf"'

    pisa.CreatePDF(r.text, dest=pdf_buffer)

    return pdf_buffer.getvalue()

# This must be added in order to do correct path lookups for the views
import os
from bottle import TEMPLATE_PATH

TEMPLATE_PATH.append(os.path.join(os.environ['OPENSHIFT_REPO_DIR'], 'wsgi/views/'))

application = default_app()
