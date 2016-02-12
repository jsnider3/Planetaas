"""
  Provides info about planets next to pretty pictures.
  @author Josh Snider
"""

from flask import Flask
from flask import render_template
app = Flask(__name__)


@app.route('/')
def main_page():
  """Show the homepage"""
  return render_template('home.html',
    img_url='http://www.jpl.nasa.gov/images/kepler/20120111/pia15257-640.jpg')

@app.route('/planet/<planet>')
def planet_page(planet):
  return render_template('planet.html',
    img_url='http://www.jpl.nasa.gov/images/kepler/20120111/pia15257-640.jpg',
    planet_name=planet)

@app.route('/system/<sysname>')
def system_page(sysname):
  return render_template('system.html',
    img_url='http://www.jpl.nasa.gov/images/kepler/20120111/pia15257-640.jpg',
    system_name=sysname)

@app.errorhandler(404)
def page_not_found(e):
  """TODO custom 404 error."""
  return "Sorry, I can't find a planet at this URL.", 404


@app.errorhandler(500)
def application_error(e):
  """TODO custom 500 error."""
  return 'Sorry, unexpected error: {}'.format(e), 500
