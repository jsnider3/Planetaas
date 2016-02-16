"""
  Gets data about planets as dictionaries.
  @author Josh Snider
"""

SOL = {
    "mercury" : {
      "name" : "mercury"
      },
    "venus" : {
      "name" : "venus"
      },
    "earth" : {
      "name" : "earth"
      },
    "mars" : {
      "name" : "mars"
      },
    "jupiter" : {
      "name" : "jupiter"
      },
    "saturn" : {
      "name" : "saturn"
      },
    "uranus" : {
      "name" : "uranus"
      },
    "neptune" : {
      "name" : "neptune"
      },
    }

def get_info(planet_name):
  planet_name = planet_name.lower()
  planet = None
  if planet_name in SOL:
    planet = SOL[planet_name]
  return planet
