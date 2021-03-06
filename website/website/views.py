# Views

import os

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
from website.images import *


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
@app.route('/heatmap', methods=['POST'])
def heatmap_view():
    # Calculate paths
    image_r_path    = os.path.join(app.config['UPLOAD_FOLDER'], 'image-r')
    image_mono_path = os.path.join(app.config['UPLOAD_FOLDER'], 'image-mono')
    heatmap_path    = os.path.join(app.config['UPLOAD_FOLDER'], 'heatmap.png')

    # Generate heatmap
    heatmap(image_r_path, image_mono_path, heatmap_path)

    # Send response
    return render_template('index.html',
                           title='Heatmap generated successfully')


# Accept uploaded files
@app.route('/upload', methods=['POST'])
def upload_view():
    type=request.form['type']
    if type not in ['r', 'mono']:
        return 'Unknown type', 401

    # Check if the Post request has the file part
    if 'file' not in request.files:
        return redirect(request.url)
    file = request.files['file']

    if file and allowed_file(file.filename):
        filename = 'image-' + type
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))

        # Send response
        return render_template('index.html',
                               title='File uploaded correctly')

