"""
  Gets data about star systems as dictionaries.
  @author Josh Snider
"""

import csv
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
  return system

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
