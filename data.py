"""
  Data analysis functions.
  @author Josh Snider
"""

import csv
from planet import Planet
import urllib2

url = "http://exoplanetarchive.ipac.caltech.edu/cgi-bin/nstedAPI/nph-nstedAPI?table=exoplanets&select=pl_hostname,pl_letter,pl_orbper,pl_orbsmax,pl_orbeccen,pl_orbincl,pl_radj,pl_dens,pl_eqt"
response = urllib2.urlopen(url)
cr = csv.reader(response)

planets = []
for row in cr:
    planets.append(Planet(row))

dicts = [dict(planet) for planet in planets]
num = len(dicts)
for key in dicts[0]:
  print (key, float(len([1 for dic in dicts if key in dic])) / num)

