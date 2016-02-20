"""
  Gets data about star systems as dictionaries.
  @author Josh Snider
"""

import csv
import hashlib
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

def get_factoid(system_name):
  ''' Return a fun fact about the given star system. '''
  facts = ['Voted most likely to go supernova!',
    'Now with 20% more Kerbals!',
    'Contains herbal helium!',
    'A good source of vitamin D!',
    '#1 rated vacation spot!',
    'Only 15 parsecs from the Kessel run!',
    'Non-allergenic, Gluten-free, and Vegan-safe!',
    'Beautiful methane sunsets!',
    'As seen on spectrogram!']

  index = int(hashlib.md5(system_name).hexdigest(), 16) % len(facts)
  return facts[index]

def get_info(system_name):
  ''' Get all the info about a system needed to display it. '''
  system_name = system_name.lower()
  planets = None
  if system_name == "sol":
    planets = SOL
  else:
    planets = get_exoplanets(system_name)
    print([str(planet) for planet in planets])
  info = None
  if planets:
    info = {}
    info['name'] = system_name
    info['planets'] = planets
    info['star'] = {"size": 20, "color": "yellow"}
    info['orbits'] = [get_orbit(planet) for planet in planets]
    info['fact'] = get_factoid(system_name)
  return info

def get_orbit(planet):
  ''' Get the svg orbit for a planet. '''
  orbit = {}
  orbit['major'] = 80
  orbit['minor'] = 40
  orbit['rot'] = 45
  return orbit

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
