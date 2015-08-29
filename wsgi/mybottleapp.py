from bottle import route, default_app, request, response, template
import pdfkit
import unicodedata
import time
import os

wkhtmltopdf_dir = os.path.dirname(__file__)
filename = wkhtmltopdf_dir[:-5] + '/wkhtmltopdf/wkhtmltopdf'
config = pdfkit.configuration(wkhtmltopdf=filename)
num_of_pdf = 0

HTML = """\
<html>
<head>
</head>
<body>
<strong>It works!</strong>
 {{ count }} pdf generated since restart.
</body>
"""


@route('/')
def index():
    return template(HTML, count=num_of_pdf)


@route('/pdf')
def pdf():
    url = unicodedata.normalize('NFKD', request.query.url).encode('ascii', 'ignore')
    if url and not url.isspace():
        pdf_filename = '"' + url + ' ' + time.strftime("%Y-%m-%d %H%M") + '.pdf"'

        response.content_type = 'application/pdf; charset=UTF-8'
        response.headers['Content-Disposition'] = 'attachment; filename=' + pdf_filename

        generated_pdf = pdfkit.from_url(url, False, configuration=config)
        global num_of_pdf
        num_of_pdf += 1
        return generated_pdf
    else:
        raise ValueError('Please provide a url')


# This must be added in order to do correct path lookups for the views
import os
from bottle import TEMPLATE_PATH

TEMPLATE_PATH.append(os.path.join(os.environ['OPENSHIFT_REPO_DIR'], 'wsgi/views/'))

application = default_app()
