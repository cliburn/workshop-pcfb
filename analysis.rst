Data analysis with Python
=========================

We have seen how to perform *data munging* with regular expressions and Python. For a refresher, here is a Python program using regular expressions to munge the ``Ch3observations.txt`` file that we did on day 1 using TextWrangler.

.. literalinclude:: /examples/regex.py

which when run produces this output

.. code-block:: console

  eris:pcfb cliburn$ python examples/regex.py 
  1752    Jan.    13      13      53      -1.414  5.781
  1961    Mar.    17      03      46      14      3.6
  2002    Oct.    1       18      22      36.51   -3.4221
  1863    Jul.    20      12      02      1.74    133

This session will introduce you to the next stage of *data analysis* and *data visualization*. Because it is impossible to do any justice to these areas in a few hours, the aim of this session is to provide a taste of what analysis and visualization in Python look like, and a tour of some of the many modules available for scientific computation in Python.

Curve Fitting
---------------------------------------

One common analysis task performed by biologists is *curve fitting*. For example, we may want to fit a 4 parameter logistic (4PL) equation to ELISA data. The usual formula for the 4PL model is 

.. math::

  f(x) = \frac{A-D}{1+(x/C)^B}+ D

where :math:`x` is the concentration, :math:`A` is the minimum asymptote, :math:`B` is the steepness, :math:`C` is the inflection point and :math:`D` is the maximum asymptote. 

.. literalinclude:: /examples/logistic.py

.. image:: /examples/logistic.png
  :scale: 75%

It will be straightforward to modify this code to use, for example, a five parameter logistic or other equation, offering a flexibility rarely available with standard analysis software.

Simulation-based statistics
-------------------------------------------

With increasing computational power, it is now feasible to run many, many simulations to estimate parameters instead of, or in addition to, the traditiional parameteric statistial methods. Most of these methods are based on some form of *resampling* of the data available to estimate the null distribution, with well known examples being the *bootstrap* and *permuation resampling*.

Before we do this, we need to understand a little about how to get random numbers. The ``numpy.random`` module has random number generators for a variety of common probabiltiy distributions. These numbers are then used to simulate the generation of new random samples. If the samples are chosen in a certain way, the statistics of the randomly drawn samples can provide useful information about the properties of our original data sample. Here are some examples of random number generation in ``iptyhon``.

.. ipython::

  In [1]: import numpy.random as npr
  
  In [2]: npr.random(5)
  Out[2]: array([ 0.81055832,  0.59554146,  0.83632506,  0.262668  ,  0.17900013])
  
  In [3]: npr.random((3,4))
  Out[3]: 
  array([[ 0.57116934,  0.09540817,  0.08523694,  0.02459664],
         [ 0.36319493,  0.55309576,  0.93008662,  0.0369388 ],
         [ 0.87274015,  0.3337237 ,  0.21890103,  0.21915681]])
  
  In [4]: npr.normal(5, 1, 4)
  Out[4]: array([ 5.17640752,  5.29399405,  4.58173086,  5.362657  ])
  
  In [5]: npr.randint(1, 7, 10)
  Out[5]: array([6, 6, 3, 5, 4, 1, 2, 5, 2, 3])
  
  In [6]: npr.uniform(1, 7, 10)
  Out[6]: 
  array([ 1.7722878 ,  6.70176442,  1.8844661 ,  2.40306296,  5.65365437,
          3.972394  ,  2.17256492,  2.3526066 ,  2.2123841 ,  3.86939384])
  
  In [7]: npr.binomial(n=10, p=0.2, size=(4,4))
  Out[7]: 
  array([[2, 1, 3, 3],
         [2, 1, 6, 1],
         [1, 4, 3, 1],
         [1, 3, 4, 3]])
  
  In [8]: x =  [1,2,3,4,5,6]
  
  In [9]: npr.shuffle(x)
  
  In [10]: x
  Out[10]: [3, 2, 5, 1, 4, 6]
  
  In [11]: npr.permutation(10)
  Out[11]: array([7, 2, 5, 4, 6, 0, 9, 8, 3, 1])
  
For example, choosing a new sample with replacement from an existing sample  (i.e. we draw one item from the data, record what it is, then replace it in the data and repeat to get a new sample)  can be done efficiently in this way:

.. ipython::

  In [1]: import numpy as np
  
  In [2]: import numpy.random as npr
  
  In [3]: data = np.array(['tom', 'jerry', 'mickey', 'minnie', 'pocahontas'])
  
  In [4]: idx = npr.randint(0, len(data), (4,len(data)))
  
  In [5]: idx
  Out[5]: 
  array([[2, 0, 2, 0, 2],
         [0, 0, 4, 3, 2],
         [1, 1, 3, 3, 3],
         [1, 4, 0, 2, 4]])
  
  In [6]: samples_with_replacement = data[idx]
  
  In [7]: samples_with_replacement
  Out[7]: 
  array([['mickey', 'tom', 'mickey', 'tom', 'mickey'],
         ['tom', 'tom', 'pocahontas', 'minnie', 'mickey'],
         ['jerry', 'jerry', 'minnie', 'minnie', 'minnie'],
         ['jerry', 'pocahontas', 'tom', 'mickey', 'pocahontas']], 
        dtype='|S10')
  
In the next version of numpy (1.7.0), a new function ``choice`` is available in ``numpy.random`` to do the same thing with a nicer syntax. Version 1.7.0 is only currently available from the git repository as source code that you must compile yourself, but should be available for easy_install/pip installation soon.

.. ipython::

  In [1]: import numpy.random as npr
  
  In [2]: data = ['tom', 'jerry', 'mickey', 'minnie', 'pocahontas']
  
  # only availlable if you install numpy 1.7.0 from the git repository
  In [3]: npr.choice(data, size=(4, len(data)), replace=True)
  Out[3]: 
  array([['pocahontas', 'tom', 'tom', 'tom', 'mickey'],
         ['minnie', 'tom', 'minnie', 'tom', 'jerry'],
         ['minnie', 'pocahontas', 'pocahontas', 'jerry', 'jerry'],
         ['mickey', 'minnie', 'jerry', 'mickey', 'tom']], 
        dtype='|S10')
  

Moving on our first simulation example - if we want to plot the 95% confidence interval for the mean of our data samples, we can use the bootstrap to do so. The basic idea is simple - draw many, many samples with replacement from the data available, estimate the mean from each sample, then rank order the means to estimate the 2.5 and 97.5 percentile values for  95% confidence interval. Unlike using normal assumptions to calculate 95% CI, the results generated by the bootstrap are robust even if the underlying data are very far from normal.

.. literalinclude:: /examples/bootstrap.py

.. image:: /examples/bootstrap.png
  :scale: 75%

Note that the bootstrap function is a *higher order* function, and will return the boostrap CI for any valid statistical function, not just the mean. For example, to find the 95% CI for the standard deviation, we only need to change ``np.mean`` to ``np.std`` in the arguments::

  # find standard deviation 95% CI bootstrap samples
  low, high =  bootstrap(x, 100000, np.std, 0.05)

The function is also highly optimized, and takes under 2 seconds to calculate the boostrap mean for a data sample of size 300 using 100,000 bootstrap samples on a 4 year old MacBook Pro with 2.4 GHz Intel Core 2 Duo processor. 

Permutation-resampling is another form of simulation-based statistical calculation, and is often used to evaluate the p-value for the difference between two groups, under the null hypothesis that the groups are invariant under label permutation. For example, in a case-control study, it can be used to find the p-value that hypothesis that the mean of the case group is different from that of the control group, and we cannot use the t-test because the distributions are highly skewed.

.. literalinclude:: /examples/resampling.py

.. image:: /examples/permutation.png
  :scale: 75%

Data visualization
----------------------------------------------

Data visualization is important for *exploratory data analysis* as well as for communication of scientific results. Using ``ipython`` with the ``-- pylab`` option provides an interarctive environment that is ideal for exploratory data analysis. The classic Anscombe data set illustrates the importance of visualization when analysing data. The Anscombe data set consists of 4 different sets of (x,y) values, with esentially *identical* values for the 

  1. mean of x
  2. variance of x
  3. mean of y
  4. variance of y
  5. correlation between x and y
  6. linear regression intercept and slope

Plotting the actual data sets quickly shows that the data sets are not as similar as suggested by the summary stattstics!

.. literalinclude:: /examples/anscombe.py

.. image:: /examples/anscombe.png
  :scale: 75%

For communication of results, matplotlib offers a huge range of graphics. We have only scratched the surface of what the package has to offer. The fastest way to get a custom graphic to communicate your results is to look at the thumbnails at http://matplotlib.sourceforge.net/gallery.html. If one of the graphics looks appropirate for your needs, just click on the thumbnail to get the source code. You should now know enough Python to customize the graphic to your specific needs.


