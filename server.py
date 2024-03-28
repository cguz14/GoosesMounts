from flask import Flask, render_template
from flask_bcrypt import Bcrypt
from model import connect_to_db
from pprint import pformat, pprint
from bs4 import BeautifulSoup as bs
from email_validator import validate_email, EmailNotValidError

from jinja2 import StrictUndefined

import os
import json
import requests
import random

app = Flask(__name__)
flask_bcrypt = Bcrypt(app)
app.secret_key = os.environ['SECRETKEY']
app.jinja_env.undefined = StrictUndefined

@app.route('/')
def homepage():
	"""Show homepage"""

	return render_template('homepage.html')

if __name__ == "__main__":
	connect_to_db(app)
	app.run() # debug=True useful on pc side while still 
	#	testing and building. Need to ensure that server side maintains lack of debug mode.
	asdfasdfasdf
	asdfa