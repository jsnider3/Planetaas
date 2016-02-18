"""
  Gets data about star systems as dictionaries.
  @author Josh Snider
"""

SOL = [{
      "name" : "mercury"
      },
      {
      "name" : "venus"
      },
      {
      "name" : "earth"
      },
      {
      "name" : "mars"
      },
      {
      "name" : "jupiter"
      },
      {
      "name" : "saturn"
      },
      {
      "name" : "uranus"
      },
      {
      "name" : "neptune"
      }
    ]

def get_info(system_name):
  system_name = system_name.lower()
  system = None
  if system_name == "sol":
    system = SOL
  return system
