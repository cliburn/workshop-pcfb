Python Basics II
================

We left out the ``while`` looping construct yesterday. It is used like this::

  initialize condition
  while (condition is True):
    do stuff
  
Typically, the *condition* is updated within the body of the while statement such that it eventually becomes false. A simple example follows:

.. ipython::

  In [1]: i = 0
  
  In [2]: while (i < 5):
     ...:     i = i+1
     ...:     print i
     ...:     
  1
  2
  3
  4
  5

Review and warm-up exercises
------------------------------------------------------------

 #. Open a terminal. What directory are you in? List the files in your current directory. Make the following new directories - ‘folder1/folder2/folder3’. Navidgate to folder2 and create a file “catted.txt” using cat with the words “I made this!.” Delete folder1, folder2 and folder3.
  
  #. Open your text editor. Load the file sequence1.txt. Find the sequences that would be cut by the EcoRI restriction enzyme that recognizes sequneces flanked on both sides by GAATTC.
  
  #. Create a list of cubes for all the positive inteters less than 10 (i.e. [1,8,27,...,729]) using a) a for loop and b) a list comprehension.
  
  #. Find all the characters that are used exactly once in the sentence 'A person who never made a mistake never tried anything new'. Ignore case, so 'A' and 'a' would be counted as 2 occurrences of 'a'.
  
  #. Find the second largest number in this list [ 9, 61,  2, 79, 58, 87, 68, 83, 61, 13]
  
  #. Make a dictionary from these two lists, using the author as the key and the quote as the value: 
  
  ``authors = ["Albert Einstein", "Richard Feynman", "Charles Darwin"]``
  
  ``quotes = ["Any man who can drive safely while kissing a pretty girl is simply not giving the kiss the attention it deserves", "There is a computer disease that anybody who works with computers knows about. It's a very serious disease and it interferes completely with the work. The trouble with computers is that you 'play' with them!", "I have tried lately to read Shakespeare, and found it so intolerably dull that it nauseated me"]``
  
  #. Write a program that generates this list [0,1,2,3,4,5,5,4,3,2,1,0]. Your program should only contain a single integer.
  
  #. Write a program that uses ``while`` and ``raw_input`` and simply repeats the question "who wins?"  until you type the words "you win". Here is a session with the program in the terminal:
  
  eris:examples cliburn$ python winner.py 
  who wins? me
  who wins? cliburn
  who wins? someone else
  who wins? you win
  
String Interpolation
------------------------------------------------------------

We start this session by learning how to construct nicely formatted strings with *holes* where we want to insert variables. The most convenient way to do this in python is by *string interpolation*. String interpolation uses codes starting with the ``%`` symbol as placeholders for inserting variables within the string. The codes that are most useful are:

  1. ``%s`` for strings
  2. ``%d`` for integers
  3. ``%f`` for floats

So for example, we can have this string:

.. ipython::

  In [125]: "%s took %d courses last year and had a %f GPA" % ('Tome', 4, 3.2)
  Out[125]: 'Tome took 4 courses last year and had a 3.200000 GPA'

Note that the variables to be inserted into the string are given as a tuple following the ``%`` separator. However, the default formatting leaves something to be desired. For numbers, we can specify the minimum width, as well as the number of decimal places when the number is a float.

.. ipython::

  In [126]: '%4d' % 123  
  Out[126]: ' 123'
  
  In [127]: '%4d' % 12345
  Out[127]: '12345'
  
  In [128]: '%5f' % 3.14
  Out[128]: '3.140000'
  
  In [129]: '%5.2f' % 3.14
  Out[129]: ' 3.14'

Sometimes it is also convenient to *pad* strings or change alignment so rows line up nicely using the flags ``0`` (left pad with zeros), `` `` (left pad with space), ``-`` (left align) and ``+`` (add sign character).

.. ipython::

  In [130]: '%05d' % 23
  Out[130]: '00023'
  
  In [131]: '% 5d' % 23
  Out[131]: '   23'
  
  In [132]: '%-5d' % 23
  Out[132]: '23   '
  
  In [133]: '%+5d' % 23
  Out[133]: '  +23'
  
Simple tables are often created using loops and string interpolation. For example, here is the code to print out the layout of a 96 well plate:

.. ipython::

  In [139]: for r in 'ABCDEF': print ' '.join(['%s%02d' % (r, c) for c in range(1, 13)])
     .....: 
  A01 A02 A03 A04 A05 A06 A07 A08 A09 A10 A11 A12
  B01 B02 B03 B04 B05 B06 B07 B08 B09 B10 B11 B12
  C01 C02 C03 C04 C05 C06 C07 C08 C09 C10 C11 C12
  D01 D02 D03 D04 D05 D06 D07 D08 D09 D10 D11 D12
  E01 E02 E03 E04 E05 E06 E07 E08 E09 E10 E11 E12
  F01 F02 F03 F04 F05 F06 F07 F08 F09 F10 F11 F12  
     
The ``join`` method of a string *joins* together all the strings in a list, separated by the original string. In this case the original string is a space ``' '``, so all the strings in the list comprehension will be joined with spaces separating them before being printed. Take your time to deconstruct this short example - it pulls together many concepts - looping, list comprehension, string interpolation and the use of the string method ``join``.

Mini-exercise
------------------------------------------------------------

1. Write a program that produces these 2 lines of output from range(1,11)::

  0001 0002 0003 0004 0005
    6.00   7.00   8.00   9.00  10.00
  
2. Write a program that starts with range(1, 6) and ends up with this string '1-one-thousand-2-one-thousand-3-one-thousand-4-one-thousand-5', using a list comprehension, the ``str()`` function and a string join.
    
Reading from and writing to files
----------------------------------------------------------

We open files using the built-in ``open`` function. We need to tell the function if the file is to be used for *reading*, *writing* or *appending* with the ``r``, ``w`` and ``a`` flags. When a file is opened for reading (the default), its contents cannot be altered. When a file is open for writing, if there is an existing file with the same name, its contents are **deleted** and you can write new content to the file. Opening for appending does not delete pre-existing file contents, but allows addition of new content appended to the existing contents. If you work with files from different operating systems, an additional useful flag is ``U`` for universal that handles differences between how Unix, Macs and Windows systems deal with line endings. All the following do the same thing - open the file ``sequnce1.txt`` in the ``examples`` directory for reading. The last version is the most robust, and will work regardless of whether ``sequnce1.txt`` was created on a Unix, Mac or Windows system, while the others only work if the file was created on the same platform as you are currently using.

.. ipython::

  In [143]: fin = open('examples/sequence1.txt')
  
  In [144]: fin = open('examples/sequence1.txt', 'r')
  
  In [145]: fin = open('examples/sequence1.txt', 'rU')
  
Opening files for writing or appending is similar, but replace the ``r`` in the argument with ``w`` or ``a``. Remember if you open the file ``sequence1.txt`` with the ``w`` flag, the current contents are gone forever.

OK. Now we will open a file for writing, write some lines, close it, open again for appending more lines, close it, and finally open again for reading.

.. ipython::

  In [180]: graffiti = '\n'.join(['Roses are red', 'Violets are blue', 'The dog is pregnant', 'Thanks to you'])

  In [160]: fo = open('graffiti.txt', 'w')
  
  In [161]: fo.write(graffiti)
  
  In [162]: fo.close()  

Here, we write some lines of doggerel in a list, join them as separate lines with the newline separator ``\n``, then write it to a file called ``directory.txt`` that has been opened for writing. Sometimes, you will see another newer idiom for opening files:

.. ipython:: python

    with open('graffiti.txt', 'w') as fo:
      fo.write(graffiti)

The difference is that when using the ``with`` statement, you don't need to remember to ``close`` the file handler. The operating system limits the numbers of file handlers that are available, and exceeding the number may lead to a system crash. Closing the file frees up the resource, but it is easy to forget to do so in more complicated programs, hence the availability of the ``with`` statement. Either way is fine. You can see what's in the file by using ``less graffiti.txt`` either in ``ipython`` or on the command line.

Let's add another line for the author of the poem:

.. ipython::

  In [163]: fo = open('graffiti.txt', 'a')
  
  In [164]: fo.write('\n' + 'by anonymous college toilet poet')
  
  In [165]: fo.close()

Note that we add a newline ``\n`` before the attribution string so that it appears on a separate line.

Mini-exercise
------------------------------------------------------------

1. Find the AT/GC ratio in ``sequence1.txt``.

2. Find all palindromes of length = 9 in ``sequence1.txt`` and save them to a file called ``palindromes.txt``.

3. Now, re-open ``palindromes.txt`` and *append* all palindromes of length 8 to the file.

Reading files with read() and readlines()
------------------------------------------------------------

We can also store the contents of the file read in by using the ``read`` and ``readlines`` methods for further processing later. The difference is that ``read`` returns the content as a single string, while ``readlines`` returns it as a list of lines.

.. ipython::

  In [45]: poem = open('graffiti.txt', 'rU').read()
  
  In [46]: poem
  Out[46]: 'Roses are red\nViolets are blue\nThe dog is pregnant\nThanks to you\nby anonymous college toilet poet'
  
  In [47]: poem = open('graffiti.txt', 'rU').readlines()
  
  In [48]: poem
  Out[48]: 
  ['Roses are red\n',
   'Violets are blue\n',
   'The dog is pregnant\n',
   'Thanks to you\n',
   'by anonymous college toilet poet']
    
We can now process the string in poem1 or the list in poem2 as necessary.

Exercise
------------------------------

1. Convert the contents of the file 'graffit.txt' to all uppercase letters. That is, calling ``cat`` or ``less`` on graffit.txt should look like this before and after your program is run:

BEFORE

.. code-block:: console

  eris:pcfb cliburn$ cat graffiti.txt 
  Roses are red
  Violets are blue
  The dog is pregnant
  Thanks to you
  by anonymous college toilet poet
  
AFTER

.. code-block:: console

  eris:pcfb cliburn$ cat graffit.txt 
  ROSES ARE RED
  VIOLETS ARE BLUE
  THE DOG IS PREGNANT
  THANKS TO YOU
  BY ANONYMOUS COLLEGE TOILET POET
  eris:pcfb cliburn$ 
  
2. ``Count the number of times each word appears in hamlet.txt found in the examples folder. For, we define a word to be any string of characters that is  separated by white space (space, tab, newline). We also ignore case - so 'ABC' is the same word as 'abc'. For extra credit, strip all punctuation before doing the word count.``

  1. Open the file 'hamlet.txt' and assign its contents to a variable as a single string
  2. Convert the string to lower case
  3. Remove all punctuation characters from the string (punctuation characters are  '!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~', which you can also find in the ``string`` module)
  4. Split the string into a list of words, where a word is defined to be any sequence of characters separated by white space
  5. Create an empty dictionary to store word counts
  6. Loop over the list of words and increment the dictionary count for that word by 1
  7. Print the number of occurrences of 'hamlet' in 'Hamlet'
  8. Close the file if necessary  

Writing your own functions
----------------------------------------------------------

We are finally in the home stretch for the Python programming module. Learning to write your own functions will greatly increase the complexity of the programs that you can write. A function is a black box - it takes some input, does something with it, and spits out some output. Functions hide details away, allowing you to solve problems at a higher level without getting bogged down. For example, consider the built-in sum function:

.. ipython::

  In [6]: numbers = [1,6,23,8,1,2,90]
  
  In [7]: sum(numbers)
  Out[7]: 131
  
The use of the built-in ``sum`` function hides the details of having to initialize the sum to zero and looping over each number while adding that number to the sum variable. While Python comes with many useful built-in functions, sooner or later, you will need to write your own functions. As you will see, writing your own functions is really simple. Let's write our version of the ``sum`` function and a ``product`` function that when given a sequence of numbers, returns the product rather than the sum of numbers. We will store save the functions in ``examples/functions.py``.

.. literalinclude:: /examples/functions.py

A typical function looks like this::

  def function_name(function_arguments):
     """Optional string describing the function."""
     statements ...
     return result

Mini-exercise
------------------------------------------------------------

1. Write a function that returns the *cumulative* sum of numbers in a list. For example, if the function is given the list [1,2,3,4,5], it should return the list [ 1,  3,  6, 10, 15].

2. Write a function ``fib`` that generates the first *n* Fibonacci numbers. The Fibonacci numbers are the sequence [1,1,2,3,5,8,13,...], where each successive number is the sum of the two preceding numbers. Here are some results that your function should give:

.. ipython::
  :suppress:

  In [9]: import sys

  In [10]: sys.path.append('examples')

  In [11]: from fib import fib

.. ipython::

  In [12]: fib(1)
  Out[12]: [1]
  
  In [13]: fib(2)
  Out[13]: [1, 1]
  
  In [14]: fib(3)
  Out[14]: [1, 1, 2]
  
  In [15]: fib(4)
  Out[15]: [1, 1, 2, 3]
  
  In [16]: fib(10)
  Out[16]: [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
    
Importing a function from a file (module)
------------------------------------------------------------

Now we can use the ``prod`` function in ``ipython`` or other programs just like a built-in function once we *import* the functions module we have just written. If we are not in the same directory as ``functions.py``, we also need to tell the Python interpreter where to find it by adding its location to the search path ``sys.path`` (which is just a list of directories that Python looks for modules). The way to *call* a function is to give the function name followed by parenthesis with values for the number of arguments expected:

.. ipython::

  In [3]: import functions
  
  In [4]: xs = [1,2,3,4]
  
  In [5]: s, p = functions.sum(xs), functions.prod(xs)
 
If calling ``functions.prod`` is too verbose for you, you can modify the import statement like so:

.. ipython

  In [207]: from functions import prod
  
  In [208]: prod(xs)
  Out[208]: 24

Just be aware that this will make any existing function with the name ``prod`` inaccessible. So for instance, if we used ``from functions import sum``, we would no longer have access to the built in ``sum`` function. Whereas if we used ``import functions``, we can choose which function to use - ``sum`` will use the built-in function, while ``functions.sum`` will use our function. We recommend using the full name all the time to avoid such *name clashes*, using a shorter alias for the imported module with the ``as`` keyword if you are really lazy.

.. ipython::

  In [209]: import functions as f
  
  In [210]: f.prod(xs)
  Out[210]: 24

Functions are first class objects
------------------------------------------------------------

In Python, functions can be treated like any other object - we can assign them to variables, use them as values in dictionaries, use them as arguments to other functions etc. 

.. ipython::

  In [4]: foo = functions.sum
  
  In [5]: foo([1,2,3])
  Out[5]: 6
  
  In [6]: func_dict = {'plus' : functions.sum, 'times' : functions.prod}
  
  In [7]: xs = [1,2,3,4]
  
  In [8]: func_dict['plus'](xs)
  Out[8]: 10
  
  In [9]: func_dict['times'](xs)
  Out[9]: 24

There is another way to write short "throwaway" functions for one-time use that is much terser using *lamba* or anonymous functions:

.. ipython::

  In [25]: f = lambda x: x*x
  
  In [26]: f(3)
  Out[26]: 9

This use of lambda is typically seen in the context of the built-in higher order functions (functions that take functions as arguments) ``map`` and ``filter``.  
  
.. ipython::

  In [23]: filter(lambda x: x % 2==0, range(10))
  Out[23]: [0, 2, 4, 6, 8]
  
  In [24]: map(lambda x: x**2, range(5))
  Out[24]: [0, 1, 4, 9, 16]

In general, Python programmers prefer to use defined rather than anonymous functions, and the use of list comprehensions rather than ``map`` and ``filter`` as they are more explicit and easier to understand, but you may come across ``lambda``, ``map`` and ``filter`` in books or on the web.

Mini-Exercise
------------------------------------

1. Replace the filter and map functionality in the above example using list comprehension.

2. Rewrite f = lambda x: x**2 as a regular function also called f using ``def``.

Function arguments
--------------------------------------
 
We can define functions with more than one argument, as well as give default values to the arguments. In turn, when *calling* a function, we can supply the arguments either by position or by name. Arguments with default values do not need to be supplied when calling a function, but if provided, will overwrite the default values.

.. ipython::

  In [1]: def f(a, b, c=3, d=100):
     ...:     print a, b, c, d
 
  In [2]: f(1,2)
  1 2 3 100
  
  In [3]: f(1,2,3,4)
  1 2 3 4
  
  In [4]: f(d=1, c=2, b=3, a=4)
  4 3 2 1

*Warning*: When you assign a list or a dictionary as a default value for an argument, the list is created at the same time the function is declared, and *persists* over subsequent function calls if not overwritten. That is probably not what you intended - if you do not want the default list to persist, you have set the default to None in the argument, then set it to the empty list in the function after checking that it has not been assigned. An example should make this clear:

.. ipython::

  # we set b to have a default of an empty list
  In [18]: def f(a, b=[]):
     ....:     b.append(a)
     ....:     print a, b
     ....:     
  
  # but the behavior is rather counter-intuitive
  In [19]: f(2)
  2 [2]
  
  In [20]: f(3)
  3 [2, 3]
  
  # if we over-write the default argument, everything is OK
  In [21]: f(3, [1,2])
  3 [1, 2, 3]
  
  # this is the way to get the non-persistent behavior
  In [22]: def f(a, b=None):
     ....:     if b is None:
     ....:         b = []
     ....:     b.append(a)
     ....:     print a, b
     ....:     
  
  In [23]: f(2)
  2 [2]
  
  In [24]: f(3)
  3 [3]
  
Exercise
-------------------------------

1. Write a function that finds palindromic sequences of length k from  a string, and use it to find all palindromic sequences of length 9  in sequence1.txt in the examples folder. The function should take 2 arguments, the string and k, the palindrome length

2. Write a program that plays the children's guessing game with you. Running the program and playing with it looks like this:

.. code-block:: console

  eris:examples cliburn$ python guessing.py 
  I'm thinking of a number between 1 and 100. Guess what it is!
  Guess a number: 50
  Too small
  Guess a number: 75
  Too large
  Guess a number: 63
  Too large
  Guess a number: 56
  Too small
  Guess a number: 60
  Too large
  Guess a number: 58
  You've guessed it! The number is 58

The first 5 lines of the program look like this:

.. code-block:: python

  import random
  
  number = random.randint(1, 101)
  guess = None
  print "I'm thinking of a number between 1 and 100. Guess what it is!"
  while guess != number:
    YOUR CODE HERE
