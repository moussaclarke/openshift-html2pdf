from bottle import route, default_app, request, response
import pdfkit
import unicodedata
import time
import os

wkhtmltopdf_dir = os.path.dirname(__file__)
filename = wkhtmltopdf_dir[:-5] + '/wkhtmltopdf/wkhtmltopdf'
config = pdfkit.configuration(wkhtmltopdf=filename)


@route('/')
def index():
    return '<strong>It works!</strong>'


@route('/pdf')
def pdf():
    url = unicodedata.normalize('NFKD', request.query.url).encode('ascii', 'ignore')
    if url and not url.isspace():
        pdf_filename = '"' + url + ' ' + time.strftime("%Y-%m-%d %H%M") + '.pdf"'

        response.content_type = 'application/pdf; charset=UTF-8'
        response.headers['Content-Disposition'] = 'attachment; filename=' + pdf_filename

        generated_pdf = pdfkit.from_url(url, False, configuration=config)
        return generated_pdf
    else:
        raise ValueError('Please provide a url')


# This must be added in order to do correct path lookups for the views
import os
from bottle import TEMPLATE_PATH

TEMPLATE_PATH.append(os.path.join(os.environ['OPENSHIFT_REPO_DIR'], 'wsgi/views/'))

application = default_app()
