import numpy as np
import numpy.random as npr
import pylab
import sys
import time

def step(x):
    """Fast life update using array shifts to add neighbors."""
    tmp = np.zeros(x.shape)
    nbrs = (
        x[:-2, 1:-1] + 
        x[:-2,  :-2] + 
        x[:-2,   2:] + 
        x[2:,  1:-1] + 
        x[2:,   :-2] +
        x[2:,    2:] + 
        x[1:-1, :-2] +
        x[1:-1,  2:]
        )
    alive = ((((nbrs==2) | (nbrs==3)) & (x[1:-1,1:-1]==1)) | # survival
             ((nbrs==3)) & (x[1:-1,1:-1]==0)) # birth
    y = x[1:-1, 1:-1]
    y[alive] = 1
    y[~alive] = 0
    tmp[1:-1, 1:-1] = y
    return tmp

numsteps = int(sys.argv[1])
gridsize = int(sys.argv[2])

x = npr.randint(0,2,(gridsize+2,gridsize+2))
fig = pylab.figure(figsize=(8,8))
ax = pylab.gca()
im = ax.imshow(x[1:-1,1:-1], interpolation='nearest')
fig.show()

start = time.clock()
for i in range(numsteps):
    x = step(x)
    im.set_data(x[1:-1,1:-1])
    fig.canvas.draw()
elapsed = time.clock() - start
print "Frames per second: %.1f" % (numsteps/elapsed)
