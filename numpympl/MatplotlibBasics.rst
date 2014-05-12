.. pcfb file, created by ARichards

===================
Matplotlib - basics
===================

Introduction
____________

The most frequently used plotting package in Python, 
`matplotlib <http://matplotlib.sourceforge.net>`_, is written
in pure Python and is heavily dependent on NumPy.  The main webpage 
`introduction <http://matplotlib.sourceforge.net/users/intro.html>`_ itemizes 
what John Hunter (mpl creator) was looking for in a plotting toolkit.  

  * Plots should look great - publication quality. One important requirement for me is that the text looks good (antialiased, etc.)
  * Postscript output for inclusion with TeX documents
  * Embeddable in a graphical user interface for application development
  * Code should be easy enough that I can understand it and extend it
  * Making plots should be easy

Matplotlib is conceptually divided into three parts:

  1. pylab interface (similar to MATLAB)  -- `pylab tutorial <http://matplotlib.sourceforge.net/users/pyplot_tutorial.html#pyplot-tutorial>`_
  2. Matplotlib **frontend** or API -- `artist tutorial <http://matplotlib.sourceforge.net/users/artists.html#artist-tutorial>`_
  3. **backends** -- drawing devices or renderers

Essentials
__________

The Axes class is the most important class in mpl.  The following three lines are used to 
get an axes class ready for use.

>>> import matplotlib.pyplot as plt
>>> fig = plt.figure()
>>> ax = fig.add_subplot(2,1,1)

If you need a freehand axis then

>>> fig2 = plt.figure()
>>> ax2 = fig2.add_axes([0.15, 0.1, 0.7, 0.3])   # [left, bottom, width, height]

After a figure is drawn you may save it and or plot it with the following.

>>> fig.saveas('foo.png',dpi=200)
>>> plt.show()

The DPI argument is optional and we can save to a bunch of formats like: JPEG, PNG, TIFF, PDF and EPS.

Here is the example from the artist tutorial.

An example
__________

.. plot:: numpympl/StandardMplExample.py
   :include-source:
