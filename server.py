from flask import Flask, render_template, request, flash, session, redirect, jsonify
from flask_bcrypt import Bcrypt
# from model import connect_to_db

from jinja2 import StrictUndefined

import os

app = Flask(__name__)
flask_bcrypt = Bcrypt(app)
app.secret_key = os.environ['SECRETKEY']
app.jinja_env.undefined = StrictUndefined

@app.route('/')
def homepage():
	"""Show homepage"""

	return render_template('homepage.html')

if __name__ == "__main__":
	# connect_to_db(app)
	app.run() 
	debug=True  # Useful on pc side while still testing and building. 
	            # Need to ensure that server side maintains lack of debug mode.