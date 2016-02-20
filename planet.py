"""
  Class that stores a planet.
  @author: Josh Snider
"""

class Planet(object):

  def __init__(self, name, fields):
    self.name = name
    self.period = fields[0]
    self.semimaj = fields[1]
    self.eccen = fields[2]
    self.incl = fields[3]
    self.radj = fields[4]
    self.dens = fields[5]
    self.eqt = fields[6]

  def __iter__(self):
    if self.name:
      yield ("name", self.name)
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


