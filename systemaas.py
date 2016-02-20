"""
  Gets data about star systems as dictionaries.
  @author Josh Snider
"""

import csv
from planet import Planet
import urllib2

SOL = [{
      "name" : "mercury",
      "radius" : "0",
      "mass" : "0",
      "orbmin" : "0",
      "orbmax" : "0"
      },
      {
      "name" : "venus",
      "radius" : "0",
      "mass" : "0",
      "orbmin" : "0",
      "orbmax" : "0"
      },
      {
      "name" : "earth",
      "radius" : "0",
      "mass" : "0",
      "orbmin" : "0",
      "orbmax" : "0"
      },
      {
      "name" : "mars",
      "radius" : "0",
      "mass" : "0",
      "orbmin" : "0",
      "orbmax" : "0"
      },
      {
      "name" : "jupiter",
      "radius" : "0",
      "mass" : "0",
      "orbmin" : "0",
      "orbmax" : "0"
      },
      {
      "name" : "saturn",
      "radius" : "0",
      "mass" : "0",
      "orbmin" : "0",
      "orbmax" : "0"
      },
      {
      "name" : "uranus",
      "radius" : "0",
      "mass" : "0",
      "orbmin" : "0",
      "orbmax" : "0"
      },
      {
      "name" : "neptune",
      "radius" : "0",
      "mass" : "0",
      "orbmin" : "0",
      "orbmax" : "0"
      }
    ]

def get_info(system_name):
  system_name = system_name.lower()
  system = None
  if system_name == "sol":
    system = SOL
  else:
    system = get_exoplanets(system_name)
    print([str(planet) for planet in system])
  return system

def get_exoplanets(system_name):
  ''' Look up data on the planets in a (non-Sol) star system. '''
  url = "http://exoplanetarchive.ipac.caltech.edu/cgi-bin/nstedAPI/nph-nstedAPI?table=exoplanets&select=pl_hostname,pl_letter,pl_orbper,pl_orbsmax,pl_orbeccen,pl_orbincl,pl_radj,pl_dens,pl_eqt"
  response = urllib2.urlopen(url)
  cr = csv.reader(response)

  planets = []
  for row in cr:
    if row[0].lower() == system_name.lower():
      planets.append(dict(Planet(row)))
  return planets

def get_systems():
  ''' Get the list of star systems with confirmed planets. '''
  systems = ['Sol']
  api_url = "http://exoplanetarchive.ipac.caltech.edu/cgi-bin/nstedAPI/nph-nstedAPI?table=exoplanets&select=distinct%20pl_hostname"
  response = urllib2.urlopen(api_url)
  cr = csv.reader(response)
  next(cr)
  for system in cr:
    systems.append(system[0])
  return systems
