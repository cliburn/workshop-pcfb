Installation and introduction
=============================

Introduction to PCfB
------------------------------------------------------------

This workshop is intended to provide an introduction to the most useful tools for computation in biology. This includes a basic command of the Unix shell, using text editors, regular expressions, scripting in the Python programming language, data management/using a relational database, and creating vector graphics for scientific communication. As there is a lot of new material to cover, we have created extensive documentation for each topic that will be accessible at this website for your reference. Please let us know if any of the documentation is unclear or has errors - we want this to be a useful resource for the future, and will fix documentation issues during the workshop itself as far as possible.

These are the specific topics that we will cover over the next few days

  #. :doc:`Basic Unix commands</unix>`
  #. :doc:`Using a text editor and regular expressions</text>`
  #. :doc:`Remote computing and web page generation</web>`
  #. :doc:`Python Basics I</python1>`
  #. :doc:`Python Basics II</python2>`
  #. :doc:`Python Modules</modules>`
  #. :doc:`NumPy and Matplotlib</numerics>`
  #. :doc:`Biopython I</biopython1>`
  #. :doc:`Biopython II</biopython2>`
  #. :doc:`Data management and relational databases</database>`
  #. :doc:`Data analysis with Python</analysis>`
  #. :doc:`Vector graphics with Inkscape</inkscape>`
  
Software installation
------------------------------------------------------------

But before we start, we just need to check that everyone has installed the required tools:

  # An operating system based on Unix (Mac or Linux)
  # A text editor that understands regular expressions
  # The Enthought Python distribution
  # A relational database system
  # Inkscape for vector graphics
  # A web account on the Duke server with public_html access
  
If any of you have had trouble installing software, we will spend some time helping you to troubleshoot. 

Feedback
------------------------------------------------------------

Preparing for and running such a workshop takes a lot of time and effort. We are therefore very interested in any feedback that you can provide that will help us improve. During the workshop, if you have any suggestions for improvement, please let us know on the spot. Since this is a small class, we want the sessions to be highly informal and welcome questions and interruptions.

We will probably run this course again in the future if you found it useful. It is also possible that we will run other similar workshops, depending on interest. As a simple survey, what computational topics would you be interested in?

  #. Practical programming for biologists - An intermediate course on the use of Python for scientific computation.
  #. Practical statistics for biologists - An introduction to basic statistics in Python and R.
  #. Practical data management for biologists - An introduction to creating and using relational database systems to manage laboratory data.
  #. Practical data visualization for biologists - An introduction to statistical and scientific graphics for exploratory data analysis and scientific communication.
  #. Modeling and simulations in biology - How to construct and simulate computational models of biological phenomena.
  #. Others (please specify)
  
Pre-test
------------------------------------------------------------

  #. Do you know how to open a Unix shell/console/terminal on your computer?
  #. How do you create a directory ``foo`` that has a subdirectory ``bar`` that has a subdirectory ``baz`` with a single command?
  #. How do you write a regular expression to find sequences that lie between specific restriction enzyme motifs?
  #. What is the difference between ``ssh`` and ``scp``?
  #. How do you write a function in Python to plot a histogram of some data?
  #. How do you use BioPython to get information from the NCBI databases?
  #. What does this mean ``select f.name, b.value from foo f, bar b where f.foo_id = b.foo_id;``?
  #. How can you estimate the 95% confidence intervals for a statistic without using any formulas?
  #. Can you illustrate a conceptual biological model using a vector graphics program?
  #. Can you write a program to summarize data from a typical laboratory spreadsheet? 
  
Record your score from 0 to 10. We are curious to see if there is any improvement in your score by the end of the workshop!
