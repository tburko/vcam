from flask import Flask

app = Flask(__name__)

import website.views
import website.config