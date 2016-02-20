"""
  Gets data about star systems as dictionaries.
  @author Josh Snider
"""

import csv
import hashlib
import pdb
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
    response = urllib.urlopen(url)
    cr = csv.reader(response)

    planets = []
    for row in cr:
      if row[0] == self.name:
        planets.append(dict(Planet(row)))
    self.planets = planets
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

  def get_orbits(self):
    ''' Get the svg orbit for the planets. '''
    orbits = []
    for planet in self.planets:
      orbit = {}
      orbit['major'] = 80
      orbit['minor'] = 40
      orbit['rot'] = 45
      orbits.append(orbit)
    return orbits

  @staticmethod
  def get_morgancolor(startype):
    ''' Gets the color of a star with given
        Morgan-Keenan classification. '''
    morgan = startype[0]
    morgan_colors = {}
    morgan_colors["O"] = "blue"
    morgan_colors["B"] = "blue"
    morgan_colors["A"] = "blue"
    morgan_colors["F"] = "white"
    morgan_colors["G"] = "yellow"
    morgan_colors["K"] = "orange"
    morgan_colors["M"] = "red"
    morgan_colors["L"] = "red"
    morgan_colors["T"] = "red"
    color = "yellow"
    if morgan in morgan_colors:
      color = morgan_colors[morgan]
    return color

  def get_stardata(self):
    ''' Look up data on the planets in a (non-Sol) star system. '''
    url = (API_BASE +
      "&select=st_spstr,st_age,st_lum" +
      "&where=" + urllib.quote("pl_hostname like '" + self.name + "'"))
    response = urllib.urlopen(url)
    cr = csv.reader(response)
    stardata = list(cr)
    result = {}
    result["size"] = 20
    result["color"] = "yellow"
    if len(stardata) > 1:
      stardata = stardata[1]
      if stardata[0]:
        result["color"] = self.get_morgancolor(stardata[0])
      if stardata[1]:
        result["age"] = stardata[1]
      if stardata[2]:
        result["size"] = result["size"] * (2 ** float(stardata[2]))
        result["size"] = min(80, result["size"])
    return result

  def to_dict(self):
    info = None
    if self.planets:
      info = {}
      info['name'] = self.name
      info['planets'] = self.planets
      info['star'] = self.get_stardata()
      info['orbits'] = self.get_orbits()
      info['fact'] = self.fact
    return info

def get_info(system_name):
  ''' Get all the info about a system needed to display it. '''
  system = System(system_name)
  if system.name.lower() == "sol":
    system.planets = SOL
  else:
    system.get_exoplanets()
    print([str(planet) for planet in system.planets])
  return system.to_dict()


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
