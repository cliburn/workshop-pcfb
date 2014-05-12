Remote computing and web page generation
========================================

Sometimes it is useful to be able to synchronize files or execute programs on a remote computer, or to transfer files from one computer to another. This can be easily done from the command line very easily using the ``ssh``, ``scp`` and ``rsync`` commands.

The ``ssh`` (secure shell) command allows you to securely connect to a remote computer for which you have access. For example, you can access your account on the Duke system:

.. code-block:: console

  eris:pcfb cliburn$ ssh ccc14@login.oit.duke.edu
  ccc14@login.oit.duke.edu's password: 
  Last login: Sat May 26 10:14:19 2012 from 152.3.189.147
  ##########################################################################
  #                                                                        # 
  #           *****   ATTENTION    *****   ATTENTION   *****               #
  #                                                                        # 
  # This is a Duke University computer system.  This computer system,      #
  # including all related equipment, networks and network devices          #
  # (includes internet access) are provided only for authorized Duke       #
  # University use. Duke University computer systems may be monitored for  #
  # all lawful purposes, including to ensure that their use is authorized, #
  # for management of the system, to facilitate protection against         #
  # unauthorized access, and to verify security procedures, survivability, #
  # and operational security. During monitoring, information may be        #
  # examined, recorded , copied , and used for authorized purposes. All    #
  # information, including personal information, placed on or sent over    #
  # this system may be monitored. use of this Duke University computer     #
  # system, authorized or unauthorized, constitutes consent to             #
  # monitoring. Unauthorized use of this Duke University computer system   #
  # may subject you to criminal prosecution. Evidence of unauthorized use  #
  # collected during monitoring may be used for administrative, criminal,  #
  # or other adverse action. Use of this system constitutes consent to     #
  # monitoring for all lawful purposes.                                    #
  ##########################################################################
  
  Self provisioned systems are now available for remote usage through OIT's Virtual Computing Lab service. To reserve your own virtual machine please visit vcl.oit.duke.edu. Additional software images will be added to this service in the coming months.
  Mon May 28 00:44:43 EDT 2012
  [ccc14@login5 ~]$ ls
  AFSDocs  public_html  Sites
  [ccc14@login5 ~]$  
  
If you know the IP address of a Linux or Mac computer that you have login rights to, you can usually connect to it via ssh. For example, this is how we typically access departmental servers or computing workstations from home. If you work with the Duke Beowulf cluster, you will also use ssh to connect and run your programs remotely.

If you can ``ssh`` to a computer, you can also copy files to or from the remote computer using ``scp`` (secure copy). Here is an example:

.. code-block:: console

  [ccc14@login5 ~]$ cat > remote.txt
  This is my remote file on lgoin.oit.duke.edu
  [ccc14@login5 ~]$ exit
  logout
  Connection to login.oit.duke.edu closed.
  eris:pcfb cliburn$ scp ccc14@login.oit.duke.edu:~/remote.txt .
  ccc14@login.oit.duke.edu's password: 
  remote.txt                                    100%   45     0.0KB/s   00:00    
  eris:pcfb cliburn$ cat remote.txt
  This is my remote file on lgoin.oit.duke.edu

If you wish to synchronize entire directory trees between computers, it is more efficient to use ``rsync`` which performs data compression, only tranfers files that are differnet, and allows resuming of interrupted transfers.  For example, ``rsync`` is a simple way to back up your files to another computer.

.. code-block:: console

  eris:tmp cliburn$ rsync -avz foo ccc14@login.oit.duke.edu:~/
  ccc14@login.oit.duke.edu's password: 
  building file list ... done
  foo/
  foo/foo.txt
  foo/bar/
  foo/bar/bar.txt
  foo/bar/baz/
  foo/bar/baz/baz.txt
  
  sent 376 bytes  received 104 bytes  73.85 bytes/sec
  total size is 75  speedup is 0.16

The flags ``-avz`` are short for ``--archive``, ``--verbose`` and ``--compress``. The ``--archive`` flag preserves symbolic links and is perfect for remote backups. As usual, you can look at ``man rsync`` if you want to know the details of how ``rsync`` works.

Web page construction with sphinx
---------------------------------------------

Sphinx (http://sphinx.pocoo.org/) is a Python tool to create documentation, but it is also great for creating highly structured webpages with minimal effort. The entire workshop website was created with Sphinx.

We start by asking Sphinx to generate the initial directory for us with the ``sphinx-quickstart`` command. The program will ask some configuration questions - you can just accept the defaults or give any sensible answer for now - the options can all be changed later if necessary.

.. code-block:: console

  eris:tmp cliburn$ sphinx-quickstart homepage
  Welcome to the Sphinx 1.1.2 quickstart utility.
  
  Please enter values for the following settings (just press Enter to
  accept a default value, if one is given in brackets).
  
  Selected root path: homepage
  
  You have two options for placing the build directory for Sphinx output.
  Either, you use a directory "_build" within the root path, or you separate
  "source" and "build" directories within the root path.
  > Separate source and build directories (y/N) [n]: 
  
  Inside the root directory, two more directories will be created; "_templates"
  for custom HTML templates and "_static" for custom stylesheets and other static
  files. You can enter another prefix (such as ".") to replace the underscore.
  > Name prefix for templates and static dir [_]: 
  
  The project name will occur in several places in the built documentation.
  > Project name: Demo home page
  > Author name(s): Cliburn Chan
  
  Sphinx has the notion of a "version" and a "release" for the
  software. Each version can have multiple releases. For example, for
  Python the version is something like 2.5 or 3.0, while the release is
  something like 2.5.1 or 3.0a1.  If you don't need this dual structure,
  just set both to the same value.
  > Project version: 0.0
  > Project release [0.0]: 
  
  The file name suffix for source files. Commonly, this is either ".txt"
  or ".rst".  Only files with this suffix are considered documents.
  > Source file suffix [.rst]: 
  
  One document is special in that it is considered the top node of the
  "contents tree", that is, it is the root of the hierarchical structure
  of the documents. Normally, this is "index", but if your "index"
  document is a custom template, you can also set this to another filename.
  > Name of your master document (without suffix) [index]: 
  
  Sphinx can also add configuration for epub output:
  > Do you want to use the epub builder (y/N) [n]: 
  
  Please indicate if you want to use one of the following Sphinx extensions:
  > autodoc: automatically insert docstrings from modules (y/N) [n]: 
  > doctest: automatically test code snippets in doctest blocks (y/N) [n]: 
  > intersphinx: link between Sphinx documentation of different projects (y/N) [n]: 
  > todo: write "todo" entries that can be shown or hidden on build (y/N) [n]: 
  > coverage: checks for documentation coverage (y/N) [n]: 
  > pngmath: include math, rendered as PNG images (y/N) [n]: 
  > mathjax: include math, rendered in the browser by MathJax (y/N) [n]: 
  > ifconfig: conditional inclusion of content based on config values (y/N) [n]: 
  > viewcode: include links to the source code of documented Python objects (y/N) [n]: 
  
  A Makefile and a Windows command file can be generated for you so that you
  only have to run e.g. `make html' instead of invoking sphinx-build
  directly.
  > Create Makefile? (Y/n) [y]: 
  > Create Windows command file? (Y/n) [y]: 
  
  Creating file homepage/conf.py.
  Creating file homepage/index.rst.
  Creating file homepage/Makefile.
  Creating file homepage/make.bat.
  
  Finished: An initial directory structure has been created.
  
  You should now populate your master file homepage/index.rst and create other documentation
  source files. Use the Makefile to build the docs, like so:
     make builder
  where "builder" is one of the supported builders, e.g. html, latex or linkcheck.
  
The next thing to do is to ``cd homepage`` to enter the directory that was just created for us and edit the ``conf.py`` file to setup a configuraiton that we like. The only change to be made for now is to change the ``html_theme`` from ``defautl`` to ``agogo`` to match our workshop website theme. The themes that come with Sphinx can be viewed at http://sphinx.pocoo.org/theming.html.

The first page to edit is the ``index.rst`` file. The ``rst`` extension is for ReStructuredText, a simple plain text markup language that is much easier to work with than HTML. Look at the primer on ReStructuredText at http://sphinx.pocoo.org/rest.html to see examples of how to use it. Open the index.rst file in your text editor::

  .. Demo home page documentation master file, created by
     sphinx-quickstart on Mon May 28 01:12:56 2012.
     You can adapt this file completely to your liking, but it should at least
     contain the root `toctree` directive.
  
  Welcome to Demo home page's documentation!
  ==========================================
  
  Contents:
  
  .. toctree::
     :maxdepth: 2
  
  
  
  Indices and tables
  ==================
  
  * :ref:`genindex`
  * :ref:`modindex`
  * :ref:`search`

Since this is to be a home page rather than documentation page, we can simplify the structure. Edit the file so that the last part looks like this::

  Contents:
  
  .. toctree::
     :maxdepth: 2
     :hidden:
  
     Home <self>
     research
     publications
  
We want to keep the table of contents *hidden*, and have set up a simple structure where the home page (index.html) links to a research.html and a publications.html file. Just as the index.html file will be generated by thiis index.rst file, the other two files are also generated by a research.rst and publications.rst file that we write using ReStructuredText. The full contents of the 3 rst files are included verbatim for reference:

index.rst
----------------------------------------
::

  Cliburn's very boring home page
  ==========================================
  
  Stuff I do
  -------------------
  
  Tongue ribeye pig, tenderloin turducken salami frankfurter strip
  steak. T-bone turducken meatball flank, beef ribs brisket corned
  beef tail. Ball tip tongue flank beef ribs, biltong tri-tip salami
  chicken sausage leberkas chuck tail. Kielbasa shankle pork chop
  sirloin, leberkas bresaola tail. Ham hamburger venison sausage
  biltong, pork loin brisket pig sirloin pastrami short loin shank
  chicken. Pig andouille leberkas beef short loin ribeye turkey ham
  hock. Cow ham kielbasa, capicola short ribs brisket shoulder
  pancetta t-bone pork belly tri-tip pork loin tenderloin.
  
  Ground round pork belly pastrami pork chop, drumstick corned beef
  t-bone tail bresaola filet mignon meatloaf. Boudin spare ribs ham
  hock short loin. Prosciutto ham hock sausage, biltong leberkas
  turkey hamburger pork meatball bresaola pork belly. Shankle tri-tip
  frankfurter ribeye leberkas ham hock, tongue beef ribs speck venison
  pork chop andouille chuck. Rump pastrami bresaola, strip steak short
  loin andouille pork chop beef boudin capicola bacon shank prosciutto
  beef ribs swine. Meatloaf leberkas pancetta beef.
  
  More stuff I do
  --------------------
  
  Enim do boudin officia labore tail. Pork exercitation short ribs
  deserunt laboris, tenderloin drumstick in dolor tongue sunt ex. Ham
  hock t-bone exercitation pork loin non mollit. Jowl boudin magna
  adipisicing in dolore. Brisket quis shoulder nostrud tempor
  ea. Aliquip officia consequat deserunt, dolore nostrud est tri-tip
  ut pancetta speck shank excepteur. Sausage cillum ground round velit
  rump, dolore laboris.
  
  Commodo consectetur ut, officia proident eu cillum jowl aute flank
  sausage ut beef ribs. Deserunt occaecat pariatur elit. Pork chop ut
  tempor, enim aliqua laborum cillum eiusmod t-bone occaecat aute
  laboris labore. Ham hock turkey beef nostrud excepteur
  dolor. Consectetur meatball chicken deserunt exercitation, corned
  beef beef in short ribs ut ea velit beef ribs. Enim andouille in,
  dolore ut meatball ea ut tail proident short ribs leberkas ground
  round filet mignon.
  
  Andouille sirloin chicken tempor aute, cow salami commodo dolore
  leberkas culpa in ea esse. Id ground round tongue velit. Ex elit
  minim sirloin fatback laboris. Irure andouille shankle cupidatat,
  nostrud bresaola id shank do jowl. Swine sirloin pork loin,
  prosciutto bresaola rump cillum in exercitation capicola.
  
  Contents:
  
  .. toctree::
     :maxdepth: 2
     :hidden:
  
     Home <self>
     research
     publications


----------

research.rst
------------------------------------------------------------
::

  Cliburn's boring research page
  =================================================
  
  Current research interests
  ---------------------------------------
  
   1. Bacon
   2. Pork rind
   3. Trotters
  
  .. image:: bacon.jpg
    :width: 60%
  
  Past research interests
  ----------------------------------------
  
   1. LOL cats
  
  .. image:: Lolcat.JPG 



publications.rst
---------------------------------------------------------------
::

  Not really Cliburn's publications
  ================================
  
  First 5 hits on Pubmed search for "Sphinx"
  ---------------------------------------------
  
    1. Quadrature RF Coil for In Vivo Brain MRI of a Macaque Monkey in
    a Stereotaxic Head Frame.  Roopnariane CA, Ryu YC, Tofighi MR,
    Miller PA, Oh S, Wang J, Park BS, Ansel L, Lieu CA, Subramanian T,
    Yang QX, Collins CM.  Concepts Magn Reson Part B Magn Reson
    Eng. 2012 Feb;41B(1):22-27. Epub 2012 Feb 18.  PMID: 22611340
    [PubMed]
    
    2. The place of general practitioners in cancer care in
    Champagne-Ardenne.  Tardieu E, Thiry-Bour C, Devaux C, Ciocan D,
    de Carvalho V, Grand M, Rousselot-Marche E, Jovenin N.  Bull
    Cancer. 2012 May 1;99(5):557-562.  PMID: 22522646 [PubMed - as
    supplied by publisher]
    
    3. Spontaneous Endometriosis in a Mandrill (Mandrillus sphinx).
    Nakamura S, Ochiai K, Ochi A, Ito M, Kamiya T, Yamamoto H.  J Comp
    Pathol. 2012 Apr 18. [Epub ahead of print] PMID: 22520805
    [PubMed - as supplied by publisher]
    
    4. [Reality of healthcare access for migrant children in Mayotte].
    Baillot J, Luminet B, Drouot N, Corty JF.  Bull Soc Pathol
    Exot. 2012 May;105(2):123-9. Epub 2012 Mar 1. French.  PMID:
    22383116 [PubMed - in process]
    
    5. Craniodental features in male Mandrillus may signal size and
    fitness: an allometric approach.  Klopp EB.  Am J Phys
    Anthropol. 2012 Apr;147(4):593-603. doi: 10.1002/ajpa.22017. Epub
    2012 Feb 10.  PMID: 22328467 [PubMed - indexed for MEDLINE]


HTML Generation
------------------------------------------------------------

With these files written, we now ask Sphinx to generate the HTML

.. code-block:: console

  eris:homepage cliburn$ make html
  sphinx-build -b html -d _build/doctrees   . _build/html
  Making output directory...
  Running Sphinx v1.1.2
  loading pickled environment... not yet created
  building [html]: targets for 3 source files that are out of date
  updating environment: 3 added, 0 changed, 0 removed
  reading sources... [100%] research                                              
  
  Not really Cliburn's publications
  ================================
  looking for now-outdated files... none found
  pickling environment... done
  checking consistency... done
  preparing documents... done
  writing output... [100%] research                                               
  writing additional files... genindex search
  copying images... [100%] bacon.jpg                                              
  copying static files... done
  dumping search index... done
  dumping object inventory... done
  build succeeded, 1 warning.
  
  Build finished. The HTML pages are in _build/html.
 
And now the directory looks like this:

.. code-block:: console

  eris:homepage cliburn$ ls
  Lolcat.JPG              _templates              make.bat
  Makefile                bacon.jpg               publications.rst
  _build                  conf.py                 research.rst
  _static                 index.rst  
  
Copy generated HTML to public_html on Duke server
------------------------------------------------------------

Now all we need to do is to ``rsync`` the ``_build/html`` folder to the Duke server:

.. code-block:: console

  eris:homepage cliburn$ rsync -avz _build/html/ ccc14@login.oit.duke.edu:~/public_html/homepage
  ccc14@login.oit.duke.edu's password: 
  building file list ... done
  created directory /afs/acpub/users/c/c/ccc14/public_html/homepage
  ./
  .buildinfo
  genindex.html
  index.html
  objects.inv
  publications.html
  research.html
  search.html
  searchindex.js
  _images/
  _images/Lolcat.JPG
  _images/bacon.jpg
  _sources/
  _sources/index.txt
  _sources/publications.txt
  _sources/research.txt
  _static/
  _static/agogo.css
  _static/ajax-loader.gif
  _static/basic.css
  _static/bgfooter.png
  _static/bgtop.png
  _static/comment-bright.png
  _static/comment-close.png
  _static/comment.png
  _static/doctools.js
  _static/down-pressed.png
  _static/down.png
  _static/file.png
  _static/jquery.js
  _static/minus.png
  _static/plus.png
  _static/pygments.css
  _static/searchtools.js
  _static/underscore.js
  _static/up-pressed.png
  _static/up.png
  _static/websupport.js
  
  sent 164472 bytes  received 792 bytes  22035.20 bytes/sec
  total size is 286369  speedup is 1.73

Now, if we navigate to http://www.duke.edu/~ccc14/homepage/, we will see the homepage and the links on the sidebar to publications and research work as well.

.. image:: /examples/homepage.png

  
