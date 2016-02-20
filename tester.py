import planetaas
import os
import subprocess
import systemaas
import unittest

class Tests(unittest.TestCase):

  def test_get_factoid(self):
    assert "vacation" in systemaas.System('sol').fact
    assert "parsecs" in systemaas.System('kepler-174').fact

  def test_get_info(self):
    assert systemaas.get_info('Babayaga') == None
    sol = systemaas.get_info('Sol')
    assert 'name' in sol
    assert 'planets' in sol
    assert 'star' in sol
    assert 'orbits' in sol
    assert 'fact' in sol

  def test_get_systems(self):
    assert 'Sol' in systemaas.get_systems()
    assert 'WASP-98' in systemaas.get_systems()
    assert 'HD 107148' in systemaas.get_systems()
    assert 'Babayaga' not in systemaas.get_systems()

  def test_sol(self):
    assert planetaas.get_info("mErcury")["name"] == "mercury"
    assert planetaas.get_info("venus")["name"] == "venus"
    assert planetaas.get_info("Earth")["name"] == "earth"
    assert planetaas.get_info("MARS")["name"] == "mars"
    assert planetaas.get_info("Jupiter")["name"] == "jupiter"
    assert planetaas.get_info("Saturn")["name"] == "saturn"
    assert planetaas.get_info("Uranus")["name"] == "uranus"
    assert planetaas.get_info("Neptune")["name"] == "neptune"

if __name__ == '__main__':
  unittest.main()
