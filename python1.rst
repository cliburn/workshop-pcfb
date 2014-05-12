Python Basics I
===============

Why program?
------------------------------

Biology is increasingly data-rich. And the amount of data is growing exponentially, as I am sure you are all only too well aware. Wouldn't it be really nice if you had some unpaid slaves that would help you sort through your data, check for problems, find the most interesting bits, and generate pretty pictures for you to include in your next manuscript? Well, you are in luck, for the computer is a slave factory, and the slaves are called programs. And today, I have some slaves to give away ...

What can my slave do?
----------------------------------------------

In this workshop, we will focus on 3 types of jobs for our slaves that are essential whenever there is a lot of data:

1. Data munging
2. Data analysis
3. Data visualization

Data munging means taking that error-riddled, color-coded, highly redundant Excel spreadsheet that biologists love to create, and cleaning, parsing and proofing it so that it is suitable for analysis. There is a related skill of how to create persistent data stores that allow you to slice and dice well-structured data that will be briefly touched upon in the session on :doc:``Data management and relational databasesI</database>``, but will require another full workshop to cover in any depth.

Data analysis is largely about how to do statistics. We will show very simple examples of analysis in :doc:``Data analysis with Python</analysis>``, but the proper cultivation of the statistical way of thinking probably requires not just another workshop, but returning to graduate school.

Finally, there are two main reasons for data visualization - the first is for exploratory data analysis, since the human brain is highly optimized to detect patterns in pictures; and the second is for communicating results, since every biologist I've ever met is only ever interested in the figures in a paper and never the raw data. Making pictures from data for exploratory analysis and communication are covered in ``NumPy and Matplotlib</numerics>`` and the creation of schematics to illustrate concepts in :doc:``Vector graphics with Inkscape</inkscape>``.

But first - in order to tell your slave how to do these jobs, you need to think like a programmer.

Thinking like a programmer
-------------------------------

Computers are stupid. And very literal. So to be able to program, we need to tell the computer what to do in very simple language without any ambiguity. Almost all programs we will deal with involve only 5 basic operations::

  1. Get input data
  2. Store data in variables
  3. Do some calculation or check logic
  4. Repeat
  5. Generate some output
  
For now, we simply define a *variable* as a name we give to data so that we can retrieve it later. The other terms should be familiar to everyone.

For example, here is a simple example that checks if a word is a palindrome:

.. literalinclude:: /examples/python102.py
  :linenos:
 
Here is another program that makes use of these 5 concepts:

.. literalinclude:: /examples/python101.py
  :linenos:

Since the 5 operations are about all that a computer can do, even big complex projects must boil down to smaller tasks that mix and match these operations. Essentially, if you know these 5 operations, you know how to program. The rest are details.

Introducing Python
--------------------------------

We will learn to program in a language called *Python*, named after the British comedy skit *Monty Python*. Python is possibly the simplest programming language to learn and has an amazing range of libraries for just about any biomedical data processing need, making it an ideal first language for biologists to learn. When you are comfortable with Python, a very useful second language to learn is *R*, another open source language specialized for statistical analysis. 

Python is an interpreted language, meaning that instructions are executed as soon as you complete a programming statement. To see the Python interpreter in action, we will use the **IPython** interpreter, which you can start by opening a Terminal window and typing ``ipython``, after which you will see this welcome message:

.. code-block:: console

  eris:pcfb cliburn$ ipython
  Enthought Python Distribution -- http://www.enthought.com
  
  Python 2.6.6 |EPD 6.3-2 (32-bit)| (r266:84292, Sep 23 2010, 11:52:53) 
  Type "copyright", "credits" or "license" for more information.
  
  IPython 0.10.1 -- An enhanced Interactive Python.
  ?         -> Introduction and overview of IPython's features.
  %quickref -> Quick reference.
  help      -> Python's own help system.
  object?   -> Details about 'object'. ?object also works, ?? prints more.
  
There is also a vanilla ``python`` interpreter, but ``ipython`` provides so many nice features such as Unix shell integration, tab completion, history etc  that I hardly ever use the ``python`` interpreter. Try typing ``?`` in ``ipython`` to see what it offers. To exit the information screen, type ``q`` to quit. There are several ways to get more information about a Python language feature - for example, what does the python ``range`` function do? Type ``help(range)`` or ``help range`` or ``range?`` or ``?range``. 

Python as a calculator
---------------------------------------

To get comfortable with ``ipython``, let's just use it as a calculator:

.. ipython::

  In [1]: 1+2*3**2
  Out[1]: 19
  
  In [2]: 3/2
  Out[2]: 1
  
  In [3]: 3/2.0
  Out[3]: 1.5
  
  In [4]: 13 % 4
  Out[4]: 1
  
  In [5]: import math
  
  In [6]: math.pi
  Out[6]: 3.1415926535897931
  
  In [7]: math.e
  Out[7]: 2.7182818284590451
  
  In [8]: math.pi/4
  Out[8]: 0.78539816339744828
  
  In [9]: math.sin(math.pi/4)
  Out[9]: 0.70710678118654746
  
  In [10]: math.asin(math.sin(math.pi/4))
  Out[10]: 0.78539816339744817
  
  In [11]: math.sqrt(16)
  Out[11]: 4.0
  
  In [12]: 16**0.5
  Out[12]: 4.0

Note the gotcha in the [2] calculation - when both numerator and denominator are integers, the division operator returns an integer, which might not be what you want. Make either numerator or denominator a float (a number with a decimal point) as in [3] to get the usual answer.

Types
---------------------

As we have already seen in the previous example, there is a difference between ``2`` and ``2.0``. In particular, they differ in *type* - ``2`` is an integer, while ``2.0`` is a float. Types are necessary so that Python can distinguish between different *kinds* of things that may have different behaviors. Here are the most commonly used basic types in Python:

1. ``Integers`` are natural numbers, ``..., -3, -2, -1, 0, 1, 2, 3 ...``
2. ``Floats`` are "decimal" numbers e.g. ``0.01, 1e-6, math.pi`` etc
3. ``Bools`` are the values ``True`` and ``False``
4.  ``Strings`` are anything within single quotes, double quotes, or "triple" quotes such as ``'hello'``, ``"hello"``, ``'''hello'''`` and ``"""hello"""``.

While the first 3 types are atomic, *strings* are actually sequences of characters, and we can retrieve characters at specific postions by *indexing* and *slicing*. An example of how we can slice and dice sequences is useful here:

.. ipython::

  In [16]: s = "My first string"
  
  In [17]: s[0]
  Out[17]: 'M'
  
  In [18]: s[1]
  Out[18]: 'y'
  
  In [19]: s[-1]
  Out[19]: 'g'
  
  In [20]: s[0:2]
  Out[20]: 'My'
  
  In [21]: s[3:8]
  Out[21]: 'first'
  
  In [22]: s[3:8:2]
  Out[22]: 'frt'
  
  In [23]: s[::-1]
  Out[23]: 'gnirts tsrif yM'

Note that in Python, we count from *zero*, not one. Note also that a negative index means count backwards from the *end* of the sequence. 

Another type of sequence that is ubiquitous in Python programs is the ``list``, consisting of a sequence of other types delimited by square brackets ``[`` and ``]``. Unlike strings which only contain characters, list elements can be anything, including other lists. Another difference between strings and lists is that the elements in a list can be changed by assigning new values to them. In geek-speak, lists are *mutable* and strings are *immutable*. You may also see ``tuples`` which are items separated by commas, and typically delimited by ``(`` and ``)``. For the most part, we can just consider tuples to be immutable lists. A neat trick we can do with tuples is *unpacking*, perhaps easier demonstrated than explained:

.. ipython:

  In [211]: a, b, c = [1,2,3]
  
  In [212]: a
  Out[212]: 1
  
  In [213]: b
  Out[213]: 2
  
  In [214]: c
  Out[214]: 3
  
  In [215]: a, b = b, a
  
  In [216]: a
  Out[216]: 2
  
  In [217]: b
  Out[217]: 1

In the first example above, we *unpacked* the length 3 list into the variables ``a``,`` b``, ``c`` in a single statement. In the second example, we swapped the contents of ``a`` and ``b``. 

Time for more experimentation in ``ipython``:

.. ipython::

  In [40]: alist = [1,2,3.14,'foo','bar',['a','b',True]]
  
  In [41]: alist[5]
  Out[41]: ['a', 'b', True]
  
  In [42]: alist[5][2]
  Out[42]: True
  
  In [43]: alist[1] = 99
  
  In [44]: alist
  Out[44]: [1, 99, 3.1400000000000001, 'foo', 'bar', ['a', 'b', True]]
  
  In [45]: atuple = (1,2,3.14,'foo','bar',['a','b',True])
  
  In [46]: atuple[5]
  Out[46]: ['a', 'b', True]
  
  In [47]: atuple[5][2]
  Out[47]: True
  
  In [48]: atuple[1] = 99
  ---------------------------------------------------------------------------
  TypeError                                 Traceback (most recent call last)
  
  /Users/cliburn/hg/pcfb/<ipython console> in <module>()
  
  TypeError: 'tuple' object does not support item assignment
  
  In [49]: astring = "hi there"
  
  In [50]: astring[2] = 'x'
  ---------------------------------------------------------------------------
  TypeError                                 Traceback (most recent call last)
  
  /Users/cliburn/hg/pcfb/<ipython console> in <module>()
  
  TypeError: 'str' object does not support item assignment

Here the difference between *mutable* and *immutable* is clearly shown. We can grow lists in several ways - using an ``insert``, and ``append`` and list ``concatenation``. We can remove items from a list by using ``pop``, ``del`` or assigning a slice to the empty list.

.. ipython::

  In [67]: blist = []
  
  In [68]: blist.append(1)
  
  In [69]: blist.append(99)
  
  In [70]: blist = blist + [3,4,5]
  
  In [71]: blist
  Out[71]: [1, 99, 3, 4, 5]
  
  In [72]: blist[2:2] = ['a','b','c']
  
  In [73]: blist
  Out[73]: [1, 99, 'a', 'b', 'c', 3, 4, 5]
  
  In [74]: blist[2:4] = []
  
  In [75]: blist
  Out[75]: [1, 99, 'c', 3, 4, 5]
  
  In [77]: blist.pop()
  Out[77]: 5
  
  In [78]: blist
  Out[78]: [1, 99, 'c', 3, 4]
  
  In [79]: del blist[3]
  
  In [80]: blist
  Out[80]: [1, 99, 'c', 4]
  
The final basic type we will look at is the ``dictionary``. A dictionary consists of ``(key, value)`` pairs, where the key is an immutable type (e.g. a number, a string, a tuple) and the value is anything. We retrieve the value in a dictionary by using the associated key. Dictionaries are delimited by ``{`` and ``}``. For example, we can make a dictionary of email addresses:

.. ipython::

  In [81]: emails = {}
  
  In [82]: emails['cliburn'] = 'cliburn.chan@duke.edu'
  
  In [84]: emails['jacob'] = 'jacob.frelinger@duke.edu'
  
  In [85]: emails['cliburn']
  Out[85]: 'cliburn.chan@duke.edu'
  
  In [86]: emails.keys()
  Out[86]: ['jacob', 'cliburn']
  
  In [87]: emails.values()
  Out[87]: ['jacob.frelinger@duke.edu', 'cliburn.chan@duke.edu']
  
  In [88]: emails
  Out[88]: {'cliburn': 'cliburn.chan@duke.edu', 'jacob': 'jacob.frelinger@duke.edu'}

We can also think of dictionaries as fancy lists that are not restricted to consecutive integers for indexing. Note that we create dictionaries with curly braces ``{}`` but assign element to and retrieve elements from dictionaries with square brackets ``[key]``. If the key is not found in the dictionary, Python will raise a KeyError exception and abort. To avoid that, we can either check for the key before retrieval, tell Python to ignore KeyErrors in a ``try-except`` statement, or return a default value using the ``get`` method instead of ``[]`` to access the dictionary. Here are more examples of dictionary creation and usage:

.. ipython::

  In [192]: zip(['a','b','c','d'], [1,2,3,4])
  Out[192]: [('a', 1), ('b', 2), ('c', 3), ('d', 4)]
  
  In [183]: adict = dict(zip(['a','b','c','d'], [1,2,3,4]))
  
  In [184]: adict
  Out[184]: {'a': 1, 'b': 2, 'c': 3, 'd': 4}
  
  In [185]: adict['b']
  Out[185]: 2
  
  In [187]: adict.get('e', 0)
  Out[187]: 0
  
  In [188]: adict
  Out[188]: {'a': 1, 'b': 2, 'c': 3, 'd': 4}
  
  In [190]: adict.setdefault('e', 0)
  Out[190]: 0
  
  In [191]: adict
  Out[191]: {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 0}

Dictionaries can also be constructed from a list of (key, value) pairs (or 2-tuples). The ``zip`` function takes the first element from list 1 and the first element from list 2 to make a tuple, then does the same for the second element etc until one or both lists are exhausted. It is used here to construct a list of pair from two matching lists of keys and values. The ``get`` method returns the default (second) argument when the key given by its first argument is not found in the dictionary. The ``setdefault`` method does the same thing, but additionally inserts the new key / default value into the dictionary if not found. If we want to ingore missing keys but just retrieve values for valid keys, we can wrap the dictionary access in a ``try-except`` statement:

.. ipython::

  In [194]: adict
  Out[194]: {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 0}
  
  In [195]: for ch in "ajfljldjajfeljad":
     .....:     try:
     .....:         print adict[ch]
     .....:     except KeyError:
     .....:         pass
     .....:     
     .....:     
  1
  4
  1
  0
  1
  4
  
The ``pass`` keyword means "do nothing". Without the ``try-except`` statement, the program would crash with a ``KeyError` the first time ``ch`` was not found in the dictionary keys ``a, b, c, d, e``.
  
You might have noticed that we sometimes used a funny notation with a *dot* ``.`` between names, for example ``list.append(1)``. This is because Python is an *object-oriented language*, and these basic types are also *classes*. We won't discuss classes here except to note that we use the dot notation to access values (attributes) and functions (methods) associated with the class. In ``ipython``, hit the ``tab`` key after the dot to see what types are available.

.. ipython::

  In [89]: blist
  Out[89]: [1, 99, 'c', 4]
  
  In [121]: [b for b in dir(blist) if not b.startswith('_')]
  Out[121]: 
  ['append',
   'count',
   'extend',
   'index',
   'insert',
   'pop',
   'remove',
   'reverse',
   'sort']
  
The code `` [b for b in dir(blist) if not b.startswith('_')] `` is a ``list comprehension`` to show all the normal methods of the list class, filtering out methods that look like ``__xxx__``. The methods with ``__`` prefixes and suffixes are "special" internal methods that we won't use in this workshop.  You can use help to find out what ``extend``, ``index`` etc do.  The ``count``, ``reverse`` and ``sort`` methods are quite simple:

.. ipython::

  In [93]: numlist = [3,1,4,1,5,1,6,9]
  In [94]: numlist.count(1)
  Out[94]: 3
  
  In [95]: numlist.sort()
  
  In [96]: numlist
  Out[96]: [1, 1, 1, 3, 4, 5, 6, 9]
  
  In [97]: numlist.reverse()
  
  In [98]: numlist
  Out[98]: [9, 6, 5, 4, 3, 1, 1, 1]

Strings have an even longer list of methods:

.. ipython::

  In [110]: quote = "My philosophy, like color television, is all there in black and white"
  
  In [111]: [m for m in dir(quote) if not m.startswith('_')]
  Out[111]: 
  ['capitalize',
   'center',
   'count',
   'decode',
   'encode',
   'endswith',
   'expandtabs',
   'find',
   'format',
   'index',
   'isalnum',
   'isalpha',
   'isdigit',
   'islower',
   'isspace',
   'istitle',
   'isupper',
   'join',
   'ljust',
   'lower',
   'lstrip',
   'partition',
   'replace',
   'rfind',
   'rindex',
   'rjust',
   'rpartition',
   'rsplit',
   'rstrip',
   'split',
   'splitlines',
   'startswith',
   'strip',
   'swapcase',
   'title',
   'translate',
   'upper',
   'zfill']
  
  In [112]: quote.lower()
  Out[112]: 'my philosophy, like color television, is all there in black and white'
  
  In [113]: quote.upper()
  Out[113]: 'MY PHILOSOPHY, LIKE COLOR TELEVISION, IS ALL THERE IN BLACK AND WHITE'
  
  In [114]: quote.split()
  Out[114]: 
  ['My',
   'philosophy,',
   'like',
   'color',
   'television,',
   'is',
   'all',
   'there',
   'in',
   'black',
   'and',
   'white']
  
  In [115]: quote = ''.join(quote)
  In [116]: quote
  Out[116]: 'My philosophy, like color television, is all there in black and white'
  
  In [117]: quote.split(',')
  Out[117]: ['My philosophy', ' like color television', ' is all there in black and white']
  
Operators
---------------------------------------------------

We have already seen some operations, such as ``+`` and ``*`` for addition and multiplication. In addition to the numeric operators, there are also Boolean operators ``and``, ``or`` and ``not``, comparison operators ``<``, ``<=``, ``>``, ``>=``, ``==``, ``!=``, ``is`` and ``is not``, and some other operators we will not discuss here (e.g. bitwise operators). Most of these operators are quite self-evident, and if not, experimentation in the interpreter will clarify what they do:

.. ipython::

  In [5]: True and False
  Out[5]: False
  
  In [6]: True or False
  Out[6]: True
  
  In [8]: not True
  Out[8]: False
  
  In [9]: 3 == 3
  Out[9]: True
  
  In [10]: 3 == 4
  Out[10]: False
  
  In [13]: 3 != 4
  Out[13]: True
  
  In [11]: 3 > 4
  Out[11]: False
  
  In [12]: 4 > 3
  Out[12]: True
  
  In [15]: None is None
  Out[15]: True
  
  In [16]: 0 is None
  Out[16]: False
  
  In [17]: 0 is not None
  Out[17]: True
  
Control flow and loops
----------------------------------------------------

We now begin to get to the heart of programming - asking the computer to do mind-numbingly boring work many, many times. The way to perform repetitions is by *looping*, but before we go there, we will first learn about how to control the program flow with the ``if-else`` family of statements. Luckily, the ``if-else`` statement family does exactly what you'd expect it to do:

.. ipython::

  In [20]: if 'math' > 'football':
     ....:     print 'Nerds rule'
     ....:else:
     ....:     print 'Jocks rule'
  Nerds rule

The structure of the ``if-else`` statement has the form::

  if (condition is true):
    do A
  else:
    do B

Here are some more examples of the ``if-else`` family:

.. ipython::
  
  In [3]: grade = None

  In [3]: score = 86
  
  In [4]: if (score > 93):
     ...:     grade = 'A'
     ...:elif (score > 85):
     ...:     grade = 'B'
     ...:elif (score > 70):
     ...:     grade = 'C'
     ...:else:
     ...:     grade = 'D'
  
  In [5]: grade
  Out[5]: 'B'
    
As you can see, the ``if`` statement can be used by itself without an ``else`` part with the understanding that if the condition is not true, then nothing is done. If you need to make decisions based on many conditions, the ``if-[elif]-else`` form is useful, where the final optional ``else`` statement will be executed if none of the others above it are true. Note that the last example depends on the *ordering* of the conditions, and works because the ``if-elif-else`` statement works from top to bottom. See if you can figure out why the code below doesn't work as intended:

.. ipython::

  In [1]: score = 86
  
  In [2]: grade = None
  
  In [3]: if (score > 70):
     ...:     grade = 'C'
     ...:elif (score > 85):
     ...:     grade = 'B'
     ...:elif (score > 93):
     ...:     grade = 'A'
     ...:     
  
  In [4]: grade
  Out[4]: 'C'
  
OK, back to looping. There are two main ways to loop in Python using the ``for`` and ``while`` statements. The ``for`` statement goes through a sequence of items one at a time, typically performing some work on that item as it *iterates* over it. The examples below should make clear what a for loop does:

.. ipython::

  In [5]: range(10, 15)
  Out[5]: [10, 11, 12, 13, 14]
  
  In [6]: for number in range(10, 15):
     ...:     print number
     ...:     
  10
  11
  12
  13
  14
  
  In [7]: for char in 'abcde':
     ...:     print char
     ...:     
  a
  b
  c
  d
  e
  
  In [8]: for name in ['adam', 'eve']:
     ...:     print name
     ...:     
  adam
  eve
      
Remember that strings, lists, tuples and dictionaries are all sequences, and hence *iterable*. So we can use the for loop on any of these. It is getting rather tedious to use the word sequence, so from now on, I will use lists, or strings or dictionaries, but you should remember that the looping constructs work on all of them. Another Python idiom that is sometimes useful in looping is the use of ``enumerate`` to keep track of position (or index) while looping over a list. Here is how it is used:

.. ipython::


  In [6]: for i, name in enumerate(['cliburn', 'jacob', 'adam']):
     ...:     print i, name
     ...:     
  0 cliburn
  1 jacob
  2 adam
  
A common use of the for loop is to create a new list from an old one. For example, here is how you can create a list of all the squares from 10 to 15.

.. ipython::

  In [16]: squares = []
  
  In [17]: for i in range(10, 16):
     ....:     squares.append(i**2)
     ....:     
  
  In [18]: squares
  Out[18]: [100, 121, 144, 169, 196, 225]

Notice that to get the numbers ``[10,11,12,13,14,15]``, we call ``range(10, 16)`` since Python indexing includes the start but excludes the end.

We can now combine ``if`` checks with loops to *filter* lists that we are constructing, only adding items to our list if they meet certain conditions. Suppose we wanted to only collect the squares of the *odd* numbers and discard the *even* one in the previous example:

.. ipython::

  In [26]: oddsquares = []
  
  In [27]: for i in range(10, 16):
     ....:     if i%2==1:
     ....:         oddsquares.append(i**2)
     ....:         
  
  In [28]: oddsquares
  Out[28]: [121, 169, 225]

This process of looping over a sequence and collecting the items in a list, filtering by some condition if necessary, is so common that Python has a short cut way of doing it known as *list comprehension*. Here is the nicer list comprehension version of the above two examples:

.. ipython::

  In [29]: squares = [i**2 for i in range(10, 16)]
  
  In [30]: squares
  Out[30]: [100, 121, 144, 169, 196, 225]
  
  In [31]: oddsquares = [i**2 for i in range(10, 16) if i%2==1]
  
  In [32]: oddsquares
  Out[32]: [121, 169, 225]  
  
We can *nest* loops within each other - for example, to generate labels for a 96-well plate, we can do this list comprehension:

.. ipython::

  In [35]: wells = ['%s%02d' % (r, c) for r in 'ABCDEF' for c in range(1, 13)]
  
  In [36]: wells[:15]
  Out[36]: 
  ['A01',
   'A02',
   'A03',
   'A04',
   'A05',
   'A06',
   'A07',
   'A08',
   'A09',
   'A10',
   'A11',
   'A12',
   'B01',
   'B02',
   'B03']

It might be clearer to understand what is happening using the longer version of creating an empty list, then using nested for loops:

.. ipython::

  In [37]: wells = []
  
  In [38]: for r in 'ABCDEF':
     ....:     for c in range(1,13):
     ....:         wells.append('%s%02d' % (r, c))
     ....:         
  
  In [39]: wells[:15]
  Out[39]: 
  ['A01',
   'A02',
   'A03',
   'A04',
   'A05',
   'A06',
   'A07',
   'A08',
   'A09',
   'A10',
   'A11',
   'A12',
   'B01',
   'B02',
   'B03']
  
Don't worry about the funny '%02d' and '%s' bits in the code. We will explain *string interpolation* in the next session. Congratulations! You have learnt the basic building blocks of a python program. Once you complete the exercise below, we will finish off our Python crash course with I/O and creating your own functions.

Storing and re-using programs
---------------------------------

Using ``ipython`` is great for learning because of the instant feedback, but at some point you will want to save your code to use for another day. To do so, we use our text editor to write code in a file that ends with the extension '.py'. Open up a new page in TextWrangler, enter the following code::

  print "I am an expert programmer"

then save it as "expert.py". Now open a new terminal, and run the program like so:

.. code-block:: console

  eris:~ cliburn$ python expert.py 
  I am an expert programmer

You can also run Python programs from within ``ipython`` with the ``run`` keyword:

.. ipython::

  In [2]: run expert.py
  I am an expert programmer

For the above two programs to run, you need to be in the same directory as ``expert.py``. Later, Jacob will show you how to run programs in arbitrary locations. 
 
Exercise
----------------------------------

It is claimed by an interviewer that the majority of computer science graduates cannot write a correct solution to this problem (http://imranontech.com/2007/01/24/using-fizzbuzz-to-find-developers-who-grok-coding/). Are you better than the average computer science graduate?

``Write a program that prints the numbers from 1 to 100. But for multiples of three print “Fizz” instead of the number and for the multiples of five print “Buzz”. For numbers which are multiples of both three and five print “FizzBuzz”.``

You should save your program in a text editor and execute it as shown above. You can experiment within ipython, and copy and paste working code from ipython into the text editor. The instruction ``history -n startline:stopline`` shows you code in your history without the line numbers that is convient for cutting and pasting. Do it in stages - first, how do you print the numbers from 1 to 100? Next, how do you find multiples of 3? How do you change what is printed if the number is a multiple of 3? And so on ...
