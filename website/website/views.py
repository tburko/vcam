# Views

from flask import Response
from flask import session
from flask import redirect
from flask import flash
from flask import render_template
from flask import url_for
from flask import request

from website import app
from website.config import *


# Homepage
@app.route('/')
def index_view():
    # Send response
    return render_template('index.html',
                           title='Multispectral camera app homepage')

