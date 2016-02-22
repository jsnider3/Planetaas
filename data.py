"""
  Data analysis functions.
  @author Josh Snider
"""

import csv
from planet import Planet
import urllib2
import xml.etree.ElementTree as ET, urllib, gzip, io

def caltech_info():
  ''' Print out some info about the caltech data. '''
  url = "http://exoplanetarchive.ipac.caltech.edu/cgi-bin/nstedAPI/nph-nstedAPI?table=exoplanets&select=pl_hostname,pl_letter,pl_orbper,pl_orbsmax,pl_orbeccen,pl_orbincl,pl_radj,pl_dens,pl_eqt,st_spstr,st_age"
  response = urllib2.urlopen(url)
  cr = csv.reader(response)

  cols = next(cr)
  colcounts = [0]*len(cols)
  rowcount = 0
  stars = set([])
  for row in cr:
    rowcount += 1
    stars.add(row[0])
    if row[-2]:
      print(row[-2])
    for ind in range(len(row)):
      if row[ind]:
        colcounts[ind] += 1
  print("There are {0} systems with planets.".format(len(stars)))
  for ind in range(len(cols)):
    print(cols[ind], float(colcounts[ind]) / rowcount)

def oec_info():
  ''' Print out some info about the Open Exoplanet Catalogue data. '''
  url = "https://github.com/OpenExoplanetCatalogue/oec_gzip/raw/master/systems.xml.gz"
  response = urllib2.urlopen(url)
  unzipped = gzip.GzipFile(fileobj=io.BytesIO(response.read()))
  oec = ET.parse(unzipped)
  print("There are {0} systems with planets.".format(
    len(oec.findall(".//system"))))
  headers = ["name", "mass", "radius", "temperature", "eccentricity",
      "inclination", "period", "semimajoraxis"]
  colcounts = [0.0]*len(headers)
  numplanets = len(oec.findall(".//planet"))
  for planet in oec.findall(".//planet"):
    for header in headers:
      if planet.findtext(header):
        colcounts[headers.index(header)] += 1

  for header in headers:
    print(header, colcounts[headers.index(header)]/numplanets)

if __name__ == '__main__':
  oec_info()
