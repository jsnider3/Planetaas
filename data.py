"""
  Data analysis functions.
  @author Josh Snider
"""

import csv
from planet import Planet
import urllib2

url = "http://exoplanetarchive.ipac.caltech.edu/cgi-bin/nstedAPI/nph-nstedAPI?table=exoplanets&select=pl_hostname,pl_letter,pl_orbper,pl_orbsmax,pl_orbeccen,pl_orbincl,pl_radj,pl_dens,pl_eqt,st_spstr,st_age"
response = urllib2.urlopen(url)
cr = csv.reader(response)

cols = next(cr)
colcounts = [0]*len(cols)
rowcount = 0
for row in cr:
  rowcount += 1
  if row[-2]:
    print(row[-2])
  for ind in range(len(row)):
    if row[ind]:
      colcounts[ind] += 1
for ind in range(len(cols)):
  print(cols[ind], float(colcounts[ind]) / rowcount)
