Python Cheat Sheet
============================================================

Interactive sessions and executing programs
------------------------------------------------------------

You are in an interactive session is you are working within ``python`` or ``ipython``. This is great for instant feedback and trial-and-error learning.

In contrast, to execute a Python program is to write your program in a file (e.g. hello.py) using a text editor, and then to run it in the Terminal with ``python hello.py``. When you write your program in a text editor, you can re-run the program whenever you like. You can also import functions from your script to use in other Python programs.

Python types
------------------------------------------------------------

Integer
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
 (-3, 4, 27) - Convert with ``int()``

.. code-block:: python

  x = int('123') # 123
  y = int('3.9') # 3 - note that floats are truncated during conversion
  
Float
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
 (3.14, 1e-6) - Convert with ``float()``

.. code-block:: python

  x = float('123') # 123.0
  y = int('3.9') # floats are truncated, so num2 is 3

Complex
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
 (3+4j) - Convert with ``complex()``

.. code-block:: python

  x = complex('3+4j') # 3+4j
  y =complex(3) # 3+4j

Bool
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
 (True, False) - Convert with ``bool()``. Note that the following convert to False:

#. None
#. zero of any numeric type, for example, 0, 0L, 0.0, 0j.
#. any empty sequence, for example, '', (), [].
#. any empty mapping, for example, {}, set([])

Anything else converts to True.

.. code-block:: python

  x = bool(0) # False
  y = bool('abc') # True

String
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
 ('a', 'hello', "", "Hello world") - Convert with ``str()``.

.. code-block:: python

  x = str(123.4) # 123.4
  y = str([1,2,3] # '[1,2,3]'

Tuple
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
 ((2,3), (4,'a',[])) - Convert with ``tuple()``

.. code-block:: python

  x = tuple([1,2,3]) # (1,2,3)
  y = tuple('aeiou') # ('a', 'e', 'i', 'o', 'u')

List
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
 ([1,2,'a',3+4j]) - Convert with ``list()``

.. code-block:: python

  x = list((1,2,3)) # [1,2,3]
  y = list('aeiou') #['a', 'e', 'i', 'o', 'u']

Dictionary
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
 ({}, {'a': 1, 'b':2} - Convert with``dict()``

.. code-block:: python

  x = dict(['ab', [1,2]]) # {1: 2, 'a': 'b'}
  y = dict(zip('ab', [1,2])) # {'a': 1, 'b': 2}

Note that the keys in a dictionary are not in any defined order. If you need to access the keys in a defined order, use ``sorted()``.

.. ipython::

  In [12]: adict = dict(zip('edcba', '12345'))
  
  In [13]: adict
  Out[13]: {'a': '5', 'b': '4', 'c': '3', 'd': '2', 'e': '1'}
  
  In [14]: adict.keys()
  Out[14]: ['a', 'c', 'b', 'e', 'd']
  
  In [15]: sorted(adict)
  Out[15]: ['a', 'b', 'c', 'd', 'e']
  
Set
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
 (set([1,1,1,2,3])) - Convert with ``set()``

.. code-block:: python

  x = set('aardvark') # set(['a', 'k', 'r', 'd', 'v'])
  y = set([1,1,1,2,3]) # set([1, 2, 3])

Note that set eliminates duplicares. One way to find the unique elements in a list is to convert to a set and then back to a list:

.. ipython::

  In [19]: list(set([1,1,1,2,3]))
  Out[19]: [1, 2, 3]

Assigning variables
------------------------------------------------------------

.. ipython::

  In [20]: a = 23
  
  In [21]: b = 34
  
  In [22]: c = 3+4j
  
  In [23]: d = 'abc'
  
  In [24]: e = True
  
  In [25]: f = (1,2,3)
  
  In [26]: g = [a,1,'s']
  
  In [27]: h = {}
  
  In [28]: i = set([1,1,1])
  
  In [29]: x, y, z = 1, 2, 3 # unpacking

  In [30]: a, b = b, a # variable swapping

Operators
------------------------------------------------------------

Comparison operators
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

=========  =======
Operation    Meaning
=========  =======
<                        strictly less than	 
<=                      less than or equal	 
>                        strictly greater than	 
>=                      greater than or equal	 
==                      equal	 
!=                        not equal
is                         object identity	 
is not                   negated object identity	 
=========  =======

.. code-block:: python


  



