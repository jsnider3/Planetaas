"""
  Class that stores a planet.
  @author: Josh Snider
"""

class Planet(object):

  def __init__(self, name, fields):
    self.name = name
    self.period = None
    self.semimaj = None
    self.eccen = None
    self.incl = None
    self.radj = None
    self.dens = None
    self.eqt = None
    self.semimin = None
    if fields[0] != '':
      self.period = float(fields[0])
    if fields[1] != '':
      self.semimaj = float(fields[1])
    if fields[2] != '':
      self.eccen = float(fields[2])
    if fields[3] != '':
      self.incl = float(fields[3])
    if fields[4] != '':
      self.radj = float(fields[4])
    if fields[5] != '':
      self.dens = float(fields[5])
    if fields[6] != '':
      self.eqt = float(fields[6])
    if self.semimaj and self.eccen:
      self.semimin = self.semimaj * ((1 - self.eccen ** 2) ** .5)
    elif self.semimaj:
      self.semimin = self.semimaj

  def __iter__(self):
    if self.name is not None:
      yield ("name", self.name)
    if self.period is not None:
      yield ("period", self.period)
    if self.semimaj is not None:
      yield ("semimaj", self.semimaj)
    if self.eccen is not None:
      yield ("eccen", self.eccen)
    if self.incl is not None:
      yield ("incl", self.incl)
    if self.radj is not None:
      yield ("radj", self.radj)
    if self.dens is not None:
      yield ("dens", self.dens)
    if self.eqt is not None:
      yield ("eqt", self.eqt)

  def __str__(self):
    return str(dict(self))


