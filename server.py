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

@app.route('/mounts')
def all_mounts():
	"""Show All Mounts"""

	return render_template('all_mounts.html')

@app.route('/accessories')
def accessories():
	"""Show All Mounts"""

	return render_template('accessories.html')

@app.route('/Sony-32R400A')
def brand_search():
	"""Show All Mounts"""

	return render_template('Sony_32R400A.html')

if __name__ == "__main__":
	# connect_to_db(app)
	app.run()
	debug=True  # Useful on pc side while still testing and building. 
	            # Need to ensure that server side maintains lack of debug mode.