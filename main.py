"""
  Provides info about planets next to pretty pictures.
  @author Josh Snider
"""

from flask import Flask
app = Flask(__name__)


@app.route('/')
def main_page():
    """TODO"""
    return 'Welcome to Planet as a Service!'

@app.errorhandler(404)
def page_not_found(e):
    """TODO custom 404 error."""
    return "Sorry, I can't find a planet at this URL.", 404


@app.errorhandler(500)
def application_error(e):
    """TODO custom 500 error."""
    return 'Sorry, unexpected error: {}'.format(e), 500
