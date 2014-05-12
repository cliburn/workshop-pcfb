Python Modules
==============

.. to cover:
    os
    csv
    sys.argv
    glob.glob
    pickle
    math (pi, sin/cos/etc)
    re
    time/datetime
    
Python comes with many libraries covering a large variety of functions.  During this section we will look at some of them.

Recall that libraries are accessed using the *import* statement.  You can see what object a library contains by using *dir(<module>)* in ipython, and looking at *<module>.<object>.__doc__* string

.. code-block:: ipython

    In [1]: import math
    
    In [2]: print math.exp.__doc__
    exp(x)
    
    Return e raised to the power of x.

os module
---------

The os module provide a platform independent way to work with the operating system, make or remove files and directories.

.. code-block:: ipython

    In [1]: import os
    
    In [2]: print os.getcwd()
    /home/jacob

    In [3]: os.chdir('/home/jacob/baz')
    
    In [4]: os.getcwd()
    Out[4]: '/home/jacob/baz'

    In [5]: os.remove('foo')
        
    In [6]: os.chdir('/home/jacob')
    
    In [7]: os.rmdir('baz')
    


csv module
----------
The *csv* module provides readers and writers for comma separated value data.

.. code-block:: ipython

    In [1]: import csv
    
    In [2]: f = open('monty_python.csv', 'w')
    
    In [3]: cfw = csv.writer(f, dialect='excel')
    
    In [4]: cfw.writerow(['spam','spam','eggs','spam'])
    
    In [5]: cfw.writerow(['spam','spam','spam and eggs', 'spam'])
    
    In [6]: cfw.writerow(['toast'])
    
    In [7]: f.close()
    
    In [8]: cfr = csv.reader(open('monty_python.csv', 'rU'), dialect='excel')
    
    In [9]: for row in cfr:
       ...:     print ', '.join(row)
       ...:     
    spam, spam, eggs, spam
    spam, spam, spam and eggs, spam
    toast

If you'd prefer a different separator than commas the delimiter optional argument can be used

.. code-block:: ipython


   In [1]: import csv
   
   In [2]: f = open('tabbs.csv', 'rU')
   
   In [3]: csvfile = csv.reader(f, delimiter='\t')
   
   In [4]: for row in csvfile:
      ...:     print row
      ...: 
   ['1', '2', '3']
   ['2', '3', '4']
   ['4', '5', '6']


often you'll want to skip the first row in a csv file, and a simple way to do that is

.. code-block:: python

   import csv
   
   f = open('test_scores.csv', 'rU')
   csvfile = csv.reader(f)
   
   header = False
   
   for row in csvfile:
      if not header:
         header = True
      else:
         print row
   f.close()

csv excercise
^^^^^^^^^^^^^
use the test_scores.csv file to calculate the average score (colum 4) for each sex (column 2)


sys.argv
--------
The sys module contains many objects and functions for dealing with how python was compiled or called when executed.  Most significantly is argv, which is a list containing all the parameters passed on the command line when python executed, including the name of the python program in position 0. Note that all the elements of sys.argv are *strings* - if you want a number, you will have to convert it using ``int()`` or ``float()``. For example, if you want to assign the argument at position 1 as an integer variable, you can use ``n = int(sys.argv[1])``.

.. code-block:: python

    import sys
    if len(sys.argv) > 1:
      print sys.argv
    else:
      print 'no arguments passed'


.. code-block:: console

    [jacob@moku ~]$ python argv_example.py foo bar baz
    ['argv_example.py', 'foo', 'bar', 'baz']


sys.argv exercise
^^^^^^^^^^^^^^^^^
write a program that takes two arguments, your first name, and your age, and then prints out
your name and the year you were born.

glob module
-----------

The *glob* module proves the glob function to perform file globbing similar to what the unix shell provides

.. code-block:: ipython

    In [1]: import glob
    
    In [2]: for file in glob.glob('./*.txt'):
       ...:     print file
       ...:     
    C.txt
    B.txt
    A.txt
    hamlet.txt


math module
-----------
The *math* module provides common algebra and trigonometric function along with several math constants. Note that the trigonometric functions work in *radians* rather than degrees. You can convert from radians to degrees with ``math.degrees`` and vice versa with ``math.radians``.

.. code-block:: ipython

    In [1]: import math
    
    In [2]: math.e
    Out[2]: 2.718281828459045
    
    In [3]: math.pi
    Out[3]: 3.141592653589793
    
    In [4]: math.log10(100)
    Out[4]: 2.0
    
    In [5]: math.log(math.e)
    Out[5]: 1.0

    In [7]: math.cos(math.pi)
    Out[7]: -1.0
    
    In [10]: math.exp(1)
    Out[10]: 2.7182818284590455
    
    In [11]: math.pow(5,2)
    Out[11]: 25.0
 
    In [12]: math.sin(math.pi)
    Out[12]: 1.2246467991473532e-16
    
for those wondering about line 12, see floats_


re (regular expressions)
------------------------

The *re* module provides access to powerful regular expressions. Use *re.search* to determine if a pattern exists in a string, or use *re.findall* to search for all instances of a pattern in a string.

.. code-block:: ipython

    In [1]: import re
    
    In [2]: m = re.search('games', 'all fun and games')
    
    In [3]: m.group()
    Out[3]: 'games'

    In [4]: re.findall('[1234567890]+','12 drummers drumming, 11 pipers piping, 10 lords a-leaping')
    Out[4]: ['12', '11', '10']


datetime and time
-----------------

The *datetime* module provides *time* and *datetime* objects, allowing easy comparison of times and dates.

.. code-block:: ipython

    In [1]: import datetime
    
    In [2]: a = datetime.time(8,30)
    
    In [3]: b = datetime.time(9,45)
    
    In [4]: b>a

The *time* module provides simple estimates for how long a command takes.

.. code-block:: ipython

    In [1]: import time
    
    In [2]: a = time.time()
    
    In [3]: time.sleep(10)
    
    In [4]: b = time.time()
    
    In [5]: print b-a
    10.743445158


pickling and unpickling
-----------------------
The *pickle* module provides a way to save python objects to a file that you can unpickle later in a different program. This allows the saving and loading of complex objects such as classes, dictionaries etc.

.. code-block:: ipython

  In [1]: import pickle
  
  In [2]: adict = {'a': [1,2,3], 'b' : [4,5,6]}
  
  # pickle.dump takes as arguments the object to be pickled and a file handler
  In [3]: pickle.dump(adict, open('adict.pic', 'w'))
  
  # delete adict to see if loading from a pickled file works
  In [4]: del adict
  
  # adict has been deleted, so we get an error message
  In [5]: adict
  ---------------------------------------------------------------------------
  NameError                                 Traceback (most recent call last)
  /Users/cliburn/hg/pcfb/<ipython-input-5-5f470a13239f> in <module>()
  ----> 1 adict
  
  NameError: name 'adict' is not defined
  
  # load adict from pickled file
  In [6]: adict = pickle.load(open('adict.pic'))
  
  In [7]: adict
  Out[7]: {'a': [1, 2, 3], 'b': [4, 5, 6]}
  

pypi (formerly cheese shop)
---------------------------
The python community maintains a database of third party python packages.  This database
lives at pypi_\ .  Many of these packages can be installed using *pip* or *easy_install*.  In the example below, I first use easy_install to install pip, then use pip to install xlrd (a module for reading XLS files). The ``-U`` flag means that the program should *update* the installation if the module is already installed. Finally, we can also use pip to uninstall modules (but not easy_install, which is why we prefer to use pip).

.. code-block:: console

  iMac:pcfb cliburn$ easy_install -U pip
  Searching for pip
  <SNIP>
  Installed /Users/cliburn/Library/Python/2.7/site-packages/pip-1.1-py2.7.egg
  Processing dependencies for pip
  Finished processing dependencies for pip

  iMac:pcfb cliburn$ pip install -U xlrd
  Downloading/unpacking xlrd from
  <SNIP>
  Successfully installed xlrd
  Cleaning up...
  
  iMac:pcfb cliburn$ pip uninstall xlrd
  Uninstalling xlrd:
    /Users/cliburn/Library/Python/2.7/site-packages/xlrd
    /Users/cliburn/Library/Python/2.7/site-packages/xlrd-0.7.7-py2.7.egg-info
    /Users/cliburn/bin/runxlrd.py
  Proceed (y/n)? y
    Successfully uninstalled xlrd
  
Exercise
--------
Write a program that takes a number on the command line and calculates the log, square,
sin and cosine, and writes them out in a csv file.

.. _pypi: http://pypi.python.org

.. _floats: http://floating-point-gui.de/