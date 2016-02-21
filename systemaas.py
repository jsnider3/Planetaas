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

class System(object):

  def __init__(self, name):
    self.name = name
    self.fact = self.get_factoid()
    self.planets = []

  def add_planet(self, planet):
    self.planets.append(planet)

  def load_planets(self):
    ''' Load the planets for this system. '''
    if not self.planets:
      if self.name.lower() == "sol":
        self.add_planet(Planet("Mercury", [.24 * 365, .39, .2056, 7.01, .034, 5.43, 440]))
        self.add_planet(Planet("Venus", [.62 * 365, .72, .0068, 3.39, .085, 5.25, 735]))
        self.add_planet(Planet("Earth", [365, 1.0, .0167, 0, 0.089, 5.52, 288]))
        self.add_planet(Planet("Mars", [1.88 * 365, 1.52, .0934, 1.85, .048, 3.93, 218]))
        self.add_planet(Planet("Jupiter", [11.86 * 365, 5.2, .0483, 1.31, 1.00, 1.33, 123]))
        self.add_planet(Planet("Saturn", [29.46 * 365, 9.5, .0560, 2.49, .84, 0.71, 103]))
        self.add_planet(Planet("Uranus", [84.01 * 365, 19.2, .0461, 0.77, .36, 1.24, 73]))
        self.add_planet(Planet("Neptune", [164.8 * 365, 30.0, .0097, 1.77, .35, 1.67, 63]))
      else:
        self.get_exoplanets()
    return self.planets

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
        planets.append(dict(Planet(row[0] + " " + row[1], row[2:])))
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
    colors = ['blue', 'brown', 'yellow', 'aqua',
              'green', 'indigo', 'red', 'snow']
    for ind in range(len(self.planets)):
      orbit = {}
      orbit['major'] = 80
      orbit['minor'] = 40
      orbit['rot'] = 45
      orbit['color'] = colors[ind]
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
  system.load_planets()
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
