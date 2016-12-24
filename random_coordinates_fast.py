#!/usr/bin/env python

import numpy as np

N = np.int(1e6) # Number of random coordinates

rd = np.column_stack((np.random.uniform(0, 360, N), 
                      np.random.uniform(-90, 90, N)))

# Fix pole overdensity.  This trick is a LOT faster than creating a cube of
# random points and then choosing radius = 1 +/- some tolerance.

p = np.abs(np.cos(rd[:,1]*np.pi/180.))
rd = rd[np.random.choice(N, size=N, replace=True, p=p/np.sum(p))]

np.savetxt('randomcoords.ascii', rd, header='RA Dec')
