"""
  Data analysis functions.
  @author Josh Snider
"""

import csv
import urllib2

url = "http://exoplanetarchive.ipac.caltech.edu/cgi-bin/nstedAPI/nph-nstedAPI?table=exoplanets&select=pl_hostname,pl_letter,pl_orbper,pl_orbsmax,pl_orbeccen,pl_orbincl,pl_radj,pl_dens,pl_eqt"
response = urllib2.urlopen(url)
cr = csv.reader(response)

class Planet(object):

  def __init__(self, row):
    self.star = row[0] + " " + row[1]
    self.period = row[2]
    self.semimaj = row[3]
    self.eccen = row[4]
    self.incl = row[5]
    self.radj = row[6]
    self.dens = row[7]
    self.eqt = row[8]

  def __iter__(self):
    if self.star:
      yield ("name", self.star)
    if self.period:
      yield ("period", self.period)
    if self.semimaj:
      yield ("major", self.semimaj)
    if self.eccen:
      yield ("ecn", self.eccen)
    if self.incl:
      yield ("incl", self.incl)
    if self.radj:
      yield ("radj", self.radj)
    if self.dens:
      yield ("dens", self.dens)
    if self.eqt:
      yield ("eqt", self.eqt)

  def __str__(self):
    return str(dict(self))

planets = []
for row in cr:
    planets.append(Planet(row))

dicts = [dict(planet) for planet in planets]
num = len(dicts)
for key in dicts[0]:
  print (key, float(len([1 for dic in dicts if key in dic])) / num)

