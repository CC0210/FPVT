#!/usr/bin/python
# coding: utf-8

import os
os.system("sudo pip3 install flask")
os.system("sudo pip3 install connexion")
os.system("sudo pip3 install io")

from flask import (
    Flask,
    render_template,
    send_from_directory
)
import connexion
import numpy as np


# Load the model
from detector import *
#================================================================
# Run the model
YOLO()

# Create KML file
from liquidgalaxy.kml_generator import *

create_kml()

# Create the application instance
app = connexion.App(__name__, specification_dir='./')

# Read the swagger.yml file to configure the endpoints
app.add_api('swagger.yml')

# Create a URL route in our application for "/"
@app.route('/')
def home():
    """
    This function just responds to the browser ULR
    localhost:5000/

    :return:        the rendered template 'home.html'
    """
    return render_template('home.html')

# If we're running in stand alone mode, run the application
if __name__ == '__main__':
    app.run(host='10.0.2.12', port=5000, debug=True)
