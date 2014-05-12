.. pcfb file, created by ARichards

======================
NumPy - linear algebra
======================

`Linear algebra <http://en.wikipedia.org/wiki/Linear_algebra>`_ is a branch of mathematics concerned with vector spaces
and the mappings between those spaces.  NumPy has a package called `linalg <http://docs.scipy.org/doc/numpy/reference/routines.linalg.html>`_.
This page is meant only to familiarize you with the NumPy's linear algebra functions for those who are interested.

A :math:`1 \times N` dimensional vector :math:`x` 

.. math::

    x =
    \begin{pmatrix}
    x_{1}  \\
    x_{2}  \\
    \vdots \\
    x_{N}
    \end{pmatrix} 

and its transpose :math:`\mathbf{x}^{T} = (x_{1}, x_{2},\ldots,x_{N})` can be expressed in python as

>>> import numpy as np
>>> x = np.array([[1,2,3]]).T
>>> xt = x.T
>>> x.shape
(3, 1)
>>> xt.shape
(1, 3)

A **column matrix** in NumPy.

.. math::
    
    x =
    \begin{pmatrix}
    3  \\
    4  \\
    5  \\
    6  
    \end{pmatrix}

>>> x = np.array([[3,4,5,6]]).T

A **row matrix** in NumPy.

.. math::

    x =
    \begin{pmatrix}
    3 & 4 & 5 & 6
    \end{pmatrix}

>>> x = np.array([[3,4,5,6]])

General matrices you are :doc:`already familiar with <Arrays>`.

.. math::

     A_{m,n} =
    \begin{pmatrix}
     a_{1,1} & a_{1,2} & \cdots & a_{1,n} \\
     a_{2,1} & a_{2,2} & \cdots & a_{2,n} \\
     \vdots  & \vdots  & \ddots & \vdots  \\
     a_{m,1} & a_{m,2} & \cdots & a_{m,n}
    \end{pmatrix}

Common tasks
____________

Matrix determinant
^^^^^^^^^^^^^^^^^^

>>> a = np.array([[3,-9],[2,5]])
>>> np.linalg.det(a)
33.000000000000014

Matrix inverse
^^^^^^^^^^^^^^

>>> A = np.array([[-4,-2],[5,5]])
>>> A
array([[-4, -2],
       [ 5,  5]])
>>> invA = np.linalg.inv(A)
>>> invA
array([[-0.5, -0.2],
       [ 0.5,  0.4]])

>>> np.round(np.dot(A,invA))
array([[ 1.,  0.],
       [ 0.,  1.]])

Because :math:`AA^{-1} = A^{-1}A = I`.

Eigenvalues and Eigenvectors
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

>>> a = np.diag((1, 2, 3))
>>> a
array([[1, 0, 0],
       [0, 2, 0],
       [0, 0, 3]])
>>> w,v = np.linalg.eig(a)
>>> w;v
array([ 1.,  2.,  3.])
array([[ 1.,  0.,  0.],
       [ 0.,  1.,  0.],
       [ 0.,  0.,  1.]])

This is by no means a complete list---also the `SciPy <http://www.scipy.org>`_ package has additional functions if this is an area of interest.


Bibliographic notes
___________________

1. Duda, R. O., Hart, P. E. & Stork, D. G. Pattern Classification, John Wiley & Sons, Inc., 2001.
