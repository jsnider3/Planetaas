import os
import subprocess
import systemaas
import unittest

class Tests(unittest.TestCase):

  def test_get_factoid(self):
    assert "vacation" in systemaas.System('sol').fact
    assert "parsecs" in systemaas.System('kepler-174').fact

  def test_get_morgancolor(self):
    assert systemaas.System.get_morgancolor("O") == "blue"
    assert systemaas.System.get_morgancolor("B") == "blue"
    assert systemaas.System.get_morgancolor("A") == "blue"
    assert systemaas.System.get_morgancolor("F") == "white"
    assert systemaas.System.get_morgancolor("G") == "yellow"
    assert systemaas.System.get_morgancolor("K") == "orange"
    assert systemaas.System.get_morgancolor("M") == "red"
    assert systemaas.System.get_morgancolor("L") == "red"
    assert systemaas.System.get_morgancolor("T") == "red"

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

if __name__ == '__main__':
  unittest.main()
