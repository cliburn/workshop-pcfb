
import numpy as np
import numpy.random as npr
import pylab
import sys
import time

def step(x):
    """Naive life update."""
    h, w = x.shape
    y = np.zeros(x.shape)
    for i in range(1, w-1):
        for j in range(1, h-1):
            nbrs = (
                x[i-1, j-1] +
                x[i-1,   j] +
                x[i-1, j+1] +
                x[i,   j-1] +
                x[i,   j+1] +
                x[i+1, j-1] +
                x[i+1,   j] +
                x[i+1, j+1])
            if ((((nbrs == 2) or (nbrs == 3)) and (x[i, j] == 1)) or
                ((nbrs == 3) and (x[i, j] == 0))):
                y[i, j] = 1
            else:
                y[i, j] == 0
    return y

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
