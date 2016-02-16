import planetaas
import os
import subprocess
import unittest

class Tests(unittest.TestCase):

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
