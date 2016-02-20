"""
  Class that stores a planet.
  @author: Josh Snider
"""

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


