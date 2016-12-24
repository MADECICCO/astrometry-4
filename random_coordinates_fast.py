"""
This script will create a chosen number of random coordinates on the celestial sphere.
There are a few ways of doing this, but the main issue is the pole overdensity that 
arises from an unaccounted cosine term when creating a uniform grid of RA, Dec.

This script fixes the pole overdensity through weighted random sampling, where the
weight is proportional to the cosine of the absolute value of the declination.
That is, a declination of (exactly) +90 or -90 degrees will have zero weight, while
a declination of 0 has a weight of unity.  

This technique is VERY fast compared with others, such as creating a uniform random
grid on a cube and choosing points near a radius of 1.
"""

import numpy as np

N = np.int(1e6) # Number of random coordinates. This is what you choose.

rd = np.column_stack((np.random.uniform(0, 360, N), 
                      np.random.uniform(-90, 90, N)))

# Fix pole overdensity.  This trick is a LOT faster than creating a cube of
# random points and then choosing radius = 1 +/- some tolerance.

p = np.abs(np.cos(rd[:,1]*np.pi/180.))
rd = rd[np.random.choice(N, size=N, replace=True, p=p/np.sum(p))]

np.savetxt('randomcoords.ascii', rd, header='RA Dec')
