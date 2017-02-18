# Views

from flask import Response
from flask import session
from flask import redirect
from flask import flash
from flask import render_template
from flask import url_for
from flask import request
from werkzeug.utils import secure_filename

from website import app
from website.config import *
from cam import heatmap


UPLOAD_FOLDER = '/home/vcam/data'
ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg'])

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


# Homepage
@app.route('/')
def index_view():
    # Send response
    return render_template('index.html',
                           title='Multispectral camera app homepage')


# Generate heatmap
@app.route('/generate-heatmap')
def heatmap_view():
    # Generate heatmap

    # Send response
    return render_template('index.html',
                           title='Multispectral camera app homepage')


# Accept uploaded files
@app.route('/upload', methods=['POST'])
def upload_view():
    # Check if the Post request has the file part
    if 'file' not in request.files:
        return redirect(request.url)
    file = request.files['file']

    if file and allowed_file(file.filename):
        filename = 'image'
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))

        # Send response
        return render_template('index.html',
                               title='Multispectral camera app homepage')

