"""
  Gets data about star systems as dictionaries.
  @author Josh Snider
"""

import csv
import hashlib
from planet import Planet
import urllib

API_BASE = "http://exoplanetarchive.ipac.caltech.edu/cgi-bin/nstedAPI/nph-nstedAPI?table=exoplanets"
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

class System(object):

  def __init__(self, name):
    self.name = name
    self.fact = self.get_factoid()

  def get_exoplanets(self):
    ''' Look up data on the planets in a (non-Sol) star system. '''
    url = (API_BASE +
      "&select=pl_hostname,pl_letter,pl_orbper,pl_orbsmax,pl_orbeccen,pl_orbincl,pl_radj,pl_dens,pl_eqt" +
      "&where=" + urllib.quote("pl_hostname like '" + self.name + "'"))
    print(url)
    response = urllib.urlopen(url)
    cr = csv.reader(response)

    planets = []
    for row in cr:
      if row[0] == self.name:
        planets.append(dict(Planet(row)))
    return planets

  def get_factoid(self):
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

    index = int(hashlib.md5(self.name.lower()).hexdigest(), 16) % len(facts)
    return facts[index]

  def get_orbit(self, planet):
    ''' Get the svg orbit for a planet. '''
    orbit = {}
    orbit['major'] = 80
    orbit['minor'] = 40
    orbit['rot'] = 45
    return orbit

  def get_stardata(self):
    ''' Look up data on the planets in a (non-Sol) star system. '''
    return {"size": 20, "color": "yellow"}

def get_info(system_name):
  ''' Get all the info about a system needed to display it. '''
  system = System(system_name)
  planets = None
  if system.name.lower() == "sol":
    planets = SOL
  else:
    planets = system.get_exoplanets()
    print([str(planet) for planet in planets])
  info = None
  if planets:
    info = {}
    info['name'] = system.name
    info['planets'] = planets
    info['star'] = system.get_stardata()
    info['orbits'] = [system.get_orbit(planet) for planet in planets]
    info['fact'] = system.fact
  return info

def get_systems():
  ''' Get the list of star systems with confirmed planets. '''
  systems = ['Sol']
  api_url = API_BASE + "&select=" + urllib.quote("distinct pl_hostname")
  response = urllib.urlopen(api_url)
  cr = csv.reader(response)
  next(cr)
  for system in cr:
    systems.append(system[0])
  return systems
