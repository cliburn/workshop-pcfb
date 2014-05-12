.. pcfb file, created by ARichards

==============
NumPy - basics
==============

Quick reference
_______________

Here we provide a quick reference guide to the commonly used functions from the NumPy package along with
several frequently encountered examples.

+-----------------------------------+-------------------------------------------------------------+
| NumPy command                     | Note                                                        |
+===================================+=============================================================+
| a.ndim                            | returns the num. of dimensions                              |
+-----------------------------------+-------------------------------------------------------------+
| a.shape                           | returns the num. of rows and colums                         |
+-----------------------------------+-------------------------------------------------------------+
| arange(start,stop,step)           | returns a sequence vector                                   |
+-----------------------------------+-------------------------------------------------------------+
| linspace(start,stop,steps)        | returns a evenly spaced sequence in the specificed interval |
+-----------------------------------+-------------------------------------------------------------+
| dot(a,b)                          | matrix multiplication                                       |
+-----------------------------------+-------------------------------------------------------------+
| vstack([a,b])                     | stack arrays a and b vertically                             |
+-----------------------------------+-------------------------------------------------------------+
| hstack([a,b])                     | stack arrays a and b horizontally                           |
+-----------------------------------+-------------------------------------------------------------+
| where(a>x)                        | returns elements from an array depending on condition       |
+-----------------------------------+-------------------------------------------------------------+
| argsort(a)                        | returns the sorted indices of an input array                | 
+-----------------------------------+-------------------------------------------------------------+

Basic operations
________________

Arithmetic operators in NumPy work **elementwise**.
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

>>> a = np.array([3,4,5])
>>> b = np.ones(3)
>>> a - b
array([ 2.,  3.,  4.])

Something that can be tricky for people familar with other programming languages is that the * operator
**does not** carry out a matrix product.  This is done with the 
`dot <http://docs.scipy.org/doc/numpy/reference/generated/numpy.dot.html>`_ function.

>>> a = np.array([[1,2],[3,4]])
>>> b = np.array([[1,2],[3,4]])
>>> a
array([[1, 2],
       [3, 4]])
>>> b
array([[1, 2],
       [3, 4]])
>>> a * b
array([[ 1,  4],
       [ 9, 16]])
>>> np.dot(a,b)
array([[ 7, 10],
       [15, 22]])

Special addition and multiplication operators
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

>>> a = np.zeros((2,2),dtype='float')
>>> a += 5
>>> a
array([[ 5.,  5.],
       [ 5.,  5.]])
>>> a *= 5
>>> a
array([[ 25.,  25.],
       [ 25.,  25.]])
>>> a + a
array([[ 50.,  50.],
       [ 50.,  50.]])

Concatenation
^^^^^^^^^^^^^

>>> a = np.array([1,2,3])
>>> b = np.array([4,5,6])
>>> c = np.array([7,8,9])
>>> np.hstack([a,b,c])
array([1, 2, 3, 4, 5, 6, 7, 8, 9])
>>> np.vstack([a,b,c])
array([[1, 2, 3],
       [4, 5, 6],
       [7, 8, 9]])

Sorting arrays
^^^^^^^^^^^^^^

>>> x.sort()
>>> x
array([0, 0, 1, 3, 4, 5])
>>> x = np.array(([1,3,4,0,0,5]))
array([3, 4, 0, 1, 2, 5])
>>> np.argsort(x)
array([3, 4, 0, 1, 2, 5])

Common math functions
^^^^^^^^^^^^^^^^^^^^^

>>> x = np.arange(1,5)
>>> np.sqrt(x) * np.pi 
array([ 3.14159265,  4.44288294,  5.44139809,  6.28318531])
>>> 2**4
16
>>> np.power(2,4)
16
>>> np.log(np.e)
1.0
>>> x = np.arange(5)
>>> x.max() - x.min()
4

Basic operations excercise
^^^^^^^^^^^^^^^^^^^^^^^^^^

.. admonition:: Exercise

   In the following table we have expression values for 5 genes at 4 time points.
   These are completely made up data.  Although, some of the questions can be 
   easily answered by looking at the data, microarray data generally come in much 
   larger tables and if you can figure it out here the same code will work for an 
   entire gene chip.  

   +------------+----------+----------+---------+----------+
   | Gene name  | 4h       | 12h      | 24h     | 48h      |
   +============+==========+==========+=========+==========+
   | A2M        | 0.12     | 0.08     | 0.06    | 0.02     |
   +------------+----------+----------+---------+----------+
   | FOS        | 0.01     | 0.07     | 0.11    | 0.09     |
   +------------+----------+----------+---------+----------+
   | BRCA2      | 0.03     | 0.04     | 0.04    | 0.02     |
   +------------+----------+----------+---------+----------+
   | CPOX       | 0.05     | 0.09     | 0.11    | 0.14     |
   +------------+----------+----------+---------+----------+

   1. create a single array for the data (4x4)
   2. find the mean expression value *per gene*
   3. find the mean expression value *per time point*
   4. which gene has the maximum mean expression value?
   5. sort the gene names by the max expression value

.. tip:: 

   >>> geneList = np.array(["A2M", "FOS", "BRCA2","CPOX"])
   >>> values0  = np.array([0.12,0.08,0.06,0.02])
   >>> values1  = np.array([0.01,0.07,0.11,0.09])
   >>> values2  = np.array([0.03,0.04,0.04,0.02])
   >>> values3  = np.array([0.05,0.09,0.11,0.14])

Additional NumPy
________________


Indexing and Slicing
^^^^^^^^^^^^^^^^^^^^

1D arrays can be indexed in the same way a Python list can.

>>> a = np.arange(10)
>>> a[2:4]
array([2, 3])
>>> a[:10:2]
array([0, 2, 4, 6, 8])
>>> a[::-1]
array([9, 8, 7, 6, 5, 4, 3, 2, 1, 0])

Multidimensional arrays can have one index per axis

>>> x = np.arange(12).reshape(3,4)
>>> x
array([[ 0,  1,  2,  3],
       [ 4,  5,  6,  7],
       [ 8,  9, 10, 11]])
>>> x[2,3]
11
>>> x[:,1]                       # everything in the second row
array([1, 5, 9])
>>> x[1,:]                       # everything in the second column
array([4, 5, 6, 7])
>>> x[1:3,:]                     # second and third rows
array([[ 4,  5,  6,  7],
       [ 8,  9, 10, 11]])

Where
^^^^^

>>> a = np.array([1,1,1,2,2,2,3,3,3])
>>> a[a>1]
array([2, 2, 2, 3, 3, 3])
>>> a[a==3]
array([3, 3, 3])
>>> np.where(a<3)
(array([0, 1, 2, 3, 4, 5]),)
>>> np.where(a<3)[0]
array([0, 1, 2, 3, 4, 5])
>>> np.where(a>9)
(array([], dtype=int64),)

Printing
^^^^^^^^

>>> for row in x:
...     print row
... 
[0 1 2 3]
[4 5 6 7]
[ 8  9 10 11]

>>> for element in x.flat:
...     print element
... 
0
1
2
3
4
5
6
7
8
9
10
11

Copying
^^^^^^^

>>> a = np.array(['a','b','c'])
>>> b = a
>>> b[1] = 'z'
>>> a
array(['a', 'z', 'c'], 
      dtype='|S1')

>>> a = np.array(['a','b','c'])
>>> b = a.copy()
>>> b[1] = 'z'
>>> a
array(['a', 'b', 'c'], 
      dtype='|S1')

Missing data
^^^^^^^^^^^^

>>> import numpy as np
>>> from scipy.stats import nanmean 
>>> a = np.array([[1,2,3],[4,5,np.nan],[7,8,9]])
>>> a
array([[  1.,   2.,   3.],
       [  4.,   5.,  nan],
       [  7.,   8.,   9.]])
>>> columnMean = nanmean(a,axis=0)
>>> columnMean
array([ 4.,  5.,  6.])
>>> rowMean = nanmean(a,axis=1)
>>> rowMean
array([ 2. ,  4.5,  8. ])

Generating random numbers
^^^^^^^^^^^^^^^^^^^^^^^^^

>>> np.random.randint(0,10,5)      # random integers from a closed interval
array([2, 8, 3, 7, 8])
>>> np.random.normal(0,1,5)        # random numbers from a Gaussian
array([ 1.44660159, -0.35625249, -2.09994545,  0.7626487 ,  0.36353648])
>>> np.random.uniform(0,2,5)       # random numbers from a uniform distribution
array([ 0.07477679,  0.36409135,  1.42847035,  1.61242304,  0.54228665])

There are many useful functions in `random <http://docs.scipy.org/doc/numpy/reference/generated/numpy.random.html>`_
however we are showing only a few so that they will be familar when we get to plotting.
