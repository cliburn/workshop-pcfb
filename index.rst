.. Practical Computing for Biologists CFAR Workshop documentation master file, created by
   sphinx-quickstart on Wed Mar 21 15:38:48 2012.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

CFAR Workshop on *Practical Computing for Biologists*, 29 May-1 June, 2012
==========================================================================

Updates
-------

**1 June 2012** The first CFAR PCfB workshop is over. Congratulations to all participants for surviving the week, and thank you for taking the time to join us and for providing detailed feedback.  :ref:`feedback` details planned improvements in response to your suggestions. We hope to be able to offer future similar courses, and to see you there again!

**24 April 2012** Personal web space on the Duke servers is not turned on by default for DUMC perosnnel. However, if you make a request for AFS space to help@oit.duke.edu, it will be available to you within 24 hours.

**9 April 2012** The PCfB textbook is now available for collection for course participants at Room 120, Surgical Oncology Research Facility. Please read or at least scan the book before the workshop starts. There are also pre-workshop :ref:`assignments` that you will need to do. We will shortly be contacting course participants for data sets/repetitive tasks that could serve as relevant demonstrations or examples of regular expression manipulation, programming or use of relational databases.

**3 April 2012** The course is now fully subscribed, and new registrants will be placed on a wait list. Please continue to register if you are interested - if there is sufficient demand, we will plan for a second workshop. Thanks so much for your enthusiasm and support!

Introduction
------------

The CFAR Biostatistics and Computational Biology Core is conducting a *free* four-day workshop for Duke researchers to learn how to use the computer more effectively for scientific work. It is designed for people who *need to work with large and complex data sets and suspect that there is a better and faster way to get their work done*. The course will use the textbook *Practical Computing for Biologists (PCfB)* by Steven Haddock and Casey Dunn, and *CFAR is generously giving each participant a free copy of the book*. The main intent of the course is to teach researchers how to use the Unix shell, the Python programming language, databases and image manipulation tools to execute common scientific chores. An OS X system is preferred since Macs provide a Unix command line natively. Windows users can also participate by setting up Linux in an emulator (this is perfectly safe and instructions are given in the *PCfB* textbook). 

The course is designed for people trained in biology, and *no previous Unix or programming experience is necessary*. The course will be limited to 12 participants and will be held at the Surgical Oncology Research Facility (SORF) Beard Conference Room from 29 May 2012 to 1 June 2012. Please email cliburn.chan@duke.edu if you have any enquiries or wish to register for the course. Acceptance will be on a first-come first-serve basis, but CFAR investigators and their trainees will be given priority.

We will contact course participants before the workshop starts to collect your copy of *Practical Computing for Biologists*. To make it relevant for your needs, participants will also be asked to suggest computational tasks that you would like to automate or simplify, as well as to contribute data sets that are tedious to preprocess and filter manually. We will try to work these examples into the demonstrations or class assignments if at all possible. Updates and course materials will be posted at http://www.duke.edu/~ccc14/pcfb/. 

Course Description
------------------

**29 May 2012 (Tuesday)**

**AM**: Software installation and working with text editors. We will install the TextWrangler editor (jEdit for Linux users), the Enthought Python distribution (Academic license), ImageMagick, ImageJ, MySQL Community Server and MySQL Workbench. Participants are expected to install the software ahead of the workshop following instructions in *PCfB*, but help and troubleshooting will be provided in the morning session if necessary. Many operations on large file sets, especially for text data, are performed much more efficiently from the command line than from a graphical interface.  We will learn how to open a Terminal, and perform text processing, access material from the web, and write simple shell scripts to automate common tasks. 

:doc:`Installation and introduction</intro>`

:doc:`Basic Unix commands</unix>`

**PM**: We will learn to use the TextWranger/jEdit editor to understand the basics of regular expressions, and how to reformat text using regular expressions. TextWrangler/jEdit will also be used to develop programs from Day 2. We will also learn to transfer and synchronize files with remote computers from the command line, or run programs on remote computers using the command line (ssh)). We will conclude by showing how to construct a simple homepage using Sphinx and upload it to the Duke server.

:doc:`Using a text editor and regular expressions</text>`

:doc:`Remote computing and web page generation</web>`

**30 May 2012 (Wednesday)**

**AM**: Day 2 introduces you to the Python programming language, a modern dynamic language that is (relatively) easy to learn. The morning session will introduce you to the powerful IPython interpreter, where you will test out code snippets with instant feedback, and learn about the Python documentation and help system. We wil then move on to Python scripting, including decisions and loops, reading from and writing to files, and writing your own functions.

:doc:`Python Basics I</python1>`

:doc:`Python Basics II</python2>`

**PM**: The afternoon will introduce you to the most useful Python modules in the standard library, followed by an introduction to the NumPy module for numerical work, and Matplotlib for graphics.

:doc:`Python Modules</modules>`

:doc:`NumPy and Matplotlib</numerics>`

**31 May 2012 (Thursday)**

**AM**: You will learn more about Numpy and Matplotlib, together with how to use the Biopython module for sequenc and array analysis, as well as how to access the NCBI databases programmatically.

:doc:`Biopython I</biopython1>`

:doc:`Biopython II</biopython2>`

**PM**: The afternoon starts with an introduction to relational databases and how to query them using SQL, then concludes with some intermediate examples of using Python for data analysis and statistical simulation.

:doc:`Data management and relational databasesI</database>`

:doc:`Data analysis with Python</analysis>`

**01 June 2012 (Friday)**

**AM**: On the final day, we will have a tutorial for how to create scientific diagrams using the vector illustration program Inkscape. The course will conclude with working through developing a moderately complex Python program to parse, summarize and display data from a cytokine assay experiment.

:doc:`Vector graphics with Inkscape</inkscape>`

:doc:`Capstone example</capstone>`


Instructor: Cliburn Chan, Biostatistics and Bioinformatics.
-----------------------------------------------------------

Cliburn is a computational biologist whose main research interest is in data analysis and modeling of immune responses. He teaches the Introduction to the Practice of Biostatistics I & II courses for the Duke Masters in Biostatistics program, and has been programming in Python for over a decade. Other instructors will be Jacob Frelinger, a PhD student in the Computational Biology and Bioinformatics (CBB) program and Adam Richards, a postdoctoral fellow in the department of Biostatistics and Bioinformatics.


.. Contents:

.. toctree::
    :maxdepth: 2
    :hidden:

    Home <self>
    data
    assignments
    references
    participants
    intro
    unix
    text
    web
    python1
    python2
    modules
    numerics
    biopython1
    biopython2
    database
    analysis
    inkscape
    capstone
    review
    feedback

.. Indices and tables
.. ==================

.. * :ref:`genindex`
.. * :ref:`modindex`
.. * :ref:`search`

.. _webpage: ./index.html
