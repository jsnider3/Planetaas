"""
  Provides info about planets next to pretty pictures.
  @author Josh Snider
"""

from flask import Flask
from flask import render_template
app = Flask(__name__)


@app.route('/')
def main_page():
    """TODO"""
    return render_template('home.html',
        img_url='http://www.jpl.nasa.gov/images/kepler/20120111/pia15257-640.jpg')

@app.errorhandler(404)
def page_not_found(e):
    """TODO custom 404 error."""
    return "Sorry, I can't find a planet at this URL.", 404


@app.errorhandler(500)
def application_error(e):
    """TODO custom 500 error."""
    return 'Sorry, unexpected error: {}'.format(e), 500
