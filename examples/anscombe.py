import numpy as np
import pylab

xs = np.loadtxt('anscombe.txt')
for i in range(4):
    x = xs[:,i*2]
    y = xs[:,i*2+1]
    A = np.vstack([x, np.ones(len(x))]).T
    m, c = np.linalg.lstsq(A, y)[0]

    pylab.subplot(2,2,i+1)
    pylab.scatter(x, y)
    pylab.plot(x, m*x+c, 'r')
    pylab.axis([2,20,0,14])

pylab.savefig('anscombe.png')
