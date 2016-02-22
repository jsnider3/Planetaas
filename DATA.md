# Data Notes

For exoplanet data I'm getting them from
http://exoplanetarchive.ipac.caltech.edu/docs/API_exoplanet_columns.html
and thus can only do what's in those fields.

For Sol, I have limitless sources of highly accurate data.

I want to use a single format for both the solar system and other
star systems.

The following are the most relevant exoplanet fields.
* pl_orbper is orbital period.
* pl_orbsmax is semi-major axis.
* pl_orbeccen is orbit eccentricity.
* pl_orbincl is orbital inclination.
* pl_radj is radius in jupiter's.
* pl_dens is density.
* pl_eqt is equilibrium temperature.

The url to get all the confirmed planets and there value for those fields is
  "http://exoplanetarchive.ipac.caltech.edu/cgi-bin/nstedAPI/nph-nstedAPI?table=exoplanets&select=pl_hostname,pl_letter,pl_orbper,pl_orbsmax,pl_orbeccen,pl_orbincl,pl_radj,pl_dens,pl_eqt"
As per data.py these are defined at the following rates:
* pl_orbsmax = 0.9073120494335737
* pl_dens = 0.17816683831101957
* pl_orbeccen = 0.4721936148300721
* pl_radj = 0.6652935118434603
* pl_orbper = 0.9675592173017508
* pl_eqt =  0.15087538619979401
* pl_orbincl = 0.22193614830072092

The Caltech database may not be very good, it looks like there are
better versions out there.

Look into https://github.com/OpenExoplanetCatalogue/open_exoplanet_catalogue/

In conclusion, the OEC database suffers from the same weaknesses as the
Caltech database and has a less performant API. I am now back to the
originalish plan of filling in the unknown values with guesses.

One thing we could do is sort the results of the systems api by how
good the data for the systems' planets are.
