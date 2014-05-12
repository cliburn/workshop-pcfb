Basic Unix Commands
===================

Working with the file system
----------------------------

Overview:

 * cd - change directories
 * pwd - print working directory
 * mkdir - make directory
 * rmdir - remove directory
 * ls - list directory
 * cp - copy files
 * mv - move files
 * rm - remove files

Changing and Making Directories
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

*pwd* is a command that prints the current directory.  Depending on how your shell is 
configured, your current directory or part of it is displayed in your prompt (the prompt is the bit in your shell that looks like this ``iMac:pcfb cliburn$``).  Typically your shell starts you in your home directory, where you would have permissions to write and create files.  To change directories you would use *cd*, the *c*\ hange *d*\ irectory command.

.. code-block:: console

    [jacob@moku ~]$ pwd
    /home/jacob
    [jacob@moku ~]$ cd /tmp
    [jacob@moku /tmp]$ pwd
    /tmp
    [jacob@moku /tmp]$ cd
    [jacob@moku ~]$ pwd
    /home/jacob
    
You can use *cd* without specifying a directory - this returns you to your home directory. You can also use *~* as an alias for your home directory too. Creating directories uses the *mkdir* command.  If you don't specify a full path (a path starting with a /) it tries to create one in the current directory.

.. code-block:: console

    [jacob@moku ~]$ pwd
    /home/jacob
    [jacob@moku ~]$ mkdir foo
    [jacob@moku ~]$ cd foo
    [jacob@moku ~/foo]$ pwd
    /home/jacob/foo
    [jacob@moku ~/foo]$ mkdir /tmp/bar
    [jacob@moku ~/foo]$ cd /tmp/bar
    [jacob@moku /tmp/bar]$ pwd
    /tmp/bar
    
If you need to make a deep hierarchy of directories all at once, you can use the *-p* argument to *mkdir* to create all the necessary  preceding directories.

.. code-block:: console

    [jacob@moku ~]$ pwd
    /home/jacob
    [jacob@moku ~]$ cd foo
    foo: No such file or directory.
    [jacob@moku ~]$ mkdir -p foo/bar
    [jacob@moku ~]$ cd foo
    [jacob@moku ~/foo]$ cd bar
    [jacob@moku ~/foo/bar]$ pwd
    /home/jacob/foo/bar

The *rmdir* command removes directories.  Directories must be empty to be removed.  Just like *mkdir*, if a full path is not specified it tries to remove the directory from the current directory.  Similar to *mkdir*, the *-p* argument tries to remove all the preceding directories

.. code-block:: console


    [jacob@moku /tmp/bar]$ cd
    [jacob@moku ~]$ rmdir /tmp/bar
    [jacob@moku ~]$ rmdir -p foo/bar
    [jacob@moku ~]$ mkdir bar
    [jacob@moku ~]$ touch bar/foo
    [jacob@moku ~]$ rmdir bar
    rmdir: bar: Directory not empty
    
*touch* is a command that creates an empty file. We will find out about it when we look at working with files

Examining directories
^^^^^^^^^^^^^^^^^^^^^
Now that we understand directories, we'd want to look at what files the directories contain. *ls* will list the files in a directory.

.. code-block:: console
   
    [jacob@moku ~]$ ls
    A.txt   B.txt   C.txt   bar
    [jacob@moku ~]$ ls bar
    foo

Just like *mkdir*, *ls* has several useful command line options. *ls -l* will list out all the extra properties of the directory listed (file permissions, owner, last time modified). *ls -a* will list hidden files (those files whose name begin with a *.*). *ls -F* will append directories names */* and (along with other symbols after other special file types).

.. code-block:: console

    [jacob@moku ~]$ ls -l
    total 5
    -rw-r--r--  1 jacob  jacob  32 May 25 08:48 A.txt
    -rw-r--r--  1 jacob  jacob  32 May 25 08:49 B.txt
    -rw-r--r--  1 jacob  jacob  64 May 25 08:53 C.txt
    drwxr-xr-x  2 jacob  jacob   3 May 23 15:54 bar
    [jacob@moku ~]$ ls -a
    .       .cshrc      .mail_aliases   .rhosts     A.txt       bar
    ..      .login      .mailrc     .shrc       B.txt
    .bash_history   .login_conf .profile    .ssh        C.txt
    [jacob@moku ~]$ ls -laF
    total 20
    drwxr-xr-x  4 jacob  jacob    16 May 27 12:11 ./
    drwxr-xr-x  4 root   wheel     5 May 23 15:12 ../
    -rw-------  1 jacob  jacob   459 May 25 09:32 .bash_history
    -rw-r--r--  1 jacob  jacob  1014 May 23 15:12 .cshrc
    -rw-r--r--  1 jacob  jacob   257 May 23 15:12 .login
    -rw-r--r--  1 jacob  jacob   167 May 23 15:12 .login_conf
    -rw-------  1 jacob  jacob   379 May 23 15:12 .mail_aliases
    -rw-r--r--  1 jacob  jacob   339 May 23 15:12 .mailrc
    -rw-r--r--  1 jacob  jacob   753 May 23 15:12 .profile
    -rw-------  1 jacob  jacob   284 May 23 15:12 .rhosts
    -rw-r--r--  1 jacob  jacob   978 May 23 15:12 .shrc
    drwx------  2 jacob  jacob     3 May 23 16:15 .ssh/
    -rw-r--r--  1 jacob  jacob    32 May 25 08:48 A.txt
    -rw-r--r--  1 jacob  jacob    32 May 25 08:49 B.txt
    -rw-r--r--  1 jacob  jacob    64 May 25 08:53 C.txt
    drwxr-xr-x  2 jacob  jacob     3 May 23 15:54 bar/

Working with files
^^^^^^^^^^^^^^^^^^

Coping files uses the *cp* command, copying from the first argument (*source*) to the last (*destination*):

.. code-block:: console

    [jacob@moku ~]$ cp A.txt bar/A.txt
    
if the destination is a directory it copes the file into the directory.

.. code-block:: console

    [jacob@moku ~]$ cp A.txt bar/ 
    [jacob@moku ~]$ ls bar
    A.txt   foo

You can also copy multiple files at once.  *cp* will copy all the files listed on the command line into the directory specified in the last argument.

.. code-block:: console

    [jacob@moku ~]$ cp A.txt B.txt C.txt bar/
    [jacob@moku ~]$ ls bar
    A.txt   B.txt   C.txt   foo

Globbing will allow us to use many files at once rather than typing them all out explicitly. Globbing is a form of wildcards.

=========   ===========================
Glob        Effect
=========   ===========================
**\***      any number of any character
**\?**      any single character
**[abc]**   one of a, b, or c
=========   ===========================

.. code-block:: console

    [jacob@moku ~]$ cp *.txt bar/
    [jacob@moku ~]$ ls bar
    A.txt   B.txt   C.txt   foo
    
or

.. code-block:: console

    [jacob@moku ~]$ cp ?.txt bar/
    [jacob@moku ~]$ ls bar
    A.txt   B.txt   C.txt   foo

or even

.. code-block:: console

    [jacob@moku ~]$ cp [ABC].txt bar/
    [jacob@moku ~]$ ls bar
    A.txt   B.txt   C.txt   foo
    

with the *-r* command line argument you can recursively copy whole directories

.. code-block:: console

    [jacob@moku ~]$ cp -r bar foo
    [jacob@moku ~]$ ls foo
    A.txt   B.txt   C.txt   foo
    
Similar to the copy command is the move command *mv*.

.. code-block:: console

    [jacob@moku ~]$ mv A.txt foo
    [jacob@moku ~]$ mv [BC].txt foo
    [jacob@moku ~]$ mv foo/*.txt bar/
    [jacob@moku ~]$ mv foo baz 
    
To remove files, use the *rm* command.  A word of caution, there is no trash can or waste basket. Removed files are **gone**.  It is very easy to accidentally shoot your self in the foot when blindly removing files.

.. code-block:: console

    [jacob@moku ~]$ rm bar/A.txt
    [jacob@moku ~]$ rm bar/[BC].txt
    [jacob@moku ~]$ ls bar 
    foo
    [jacob@moku ~]$ rm -rf bar/
    
the *-r* command line flag removes files recursively, while *-f* attempts to ignore permissions on the file. The combination of *-r* and *-f* flags can be useful to remove whole directory tree. **BE VERY CAREFUL** using *-r* and *-f* flags.



Working with file contents
--------------------------

 * cat - concatenate command

   * pipes and redirects  - Why con\ **cat**\ enate prints to the screen
   * globbing  - Working with wildcards

 * less - a more sensible way to look at the contents of file
 * grep - searching for patterns in files

   * basics of regular expressions

Examining files
^^^^^^^^^^^^^^^
The *cat* command will display files on the screen

.. code-block:: console

    [jacob@moku ~]$ cat A.txt 
    This is file A.
    It has 2 lines.
    [jacob@moku ~]$ cat B.txt
    This is file B.
    It has
    3 lines.
    
*cat* will also concatenate files to print to the screen.

.. code-block:: console

    [jacob@moku ~]$ cat A.txt B.txt
    This is file A.
    It has 2 lines.
    This is file B.
    It has
    3 lines.

Using redirects allows us to save the concatenated file.

.. code-block:: console

    [jacob@moku ~]$ cat A.txt B.txt > C.txt
    [jacob@moku ~]$ cat C.txt
    This is file A.
    It has 2 lines.
    This is file B.
    It has
    3 lines.

*>* is a redirect to create a new file (and delete the old file if it exists). *>>* is the append redirect, while *|* (pipe) allow you to send the output of one command as input to a new command.




.. code-block:: console

    [jacob@moku ~]$ cat [AB].txt
    This is file A.
    It has 2 lines.
    This is file B.
    It has
    3 lines.

While *cat* is useful for displaying small files, longer files would page off the screen quickly. To display longer files, a page aware program will be used, *less*.

.. code-block:: console

    [jacob@moku ~]$ less <file name>
    
Common useful less keys

======  =======================
key     effect
======  =======================
G       Go to the last line
1G      Go to the first line
#G      Go to line number #
/foo    Search forward for foo
?foo    Search Backward for foo
q       Quit less
======  =======================

Quitting (or how to escape when you are lost)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
You may at some point find you self lost, and your prompt doing interesting things you don't
expect.  Here are some keys to try and get your prompt back in the state you expect.

 * q
 * Esc
 * ctrl-d (sends an end of file saying there is no more input)
 * typing Quit
 * typing exit
 * ctrl-c (sends a break, telling the program to abruptly halt)

Regexp, *grep*, and searching in files
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
The *grep* command allows you to tap into the powerful regular expression language to search the contests of file for complex patterns.

.. code-block:: console

    [jacob@moku ~]$ grep 'poor Yorick' hamlet.txt 
      Ham. Let me see. [Takes the skull.] Alas, poor Yorick! I knew him,  
      
The first argument passed to grep is the pattern to search for, in the above example `poor Yorick`.

Regular expressions provide the ability to search beyond known text, using wildcards to build complex patterns.

=====  ==========================================
key    Meaning
=====  ==========================================
.      any single character
\+      one or more of the preceding character
\*      zero or more of the preceding character
\^      matches the beginning of the line
\$      matches the end of the line
[abc]  matches a singular character of a, b, or c
=====  ==========================================

so to find all the lines beginning with the word `HAMLET` and end withs `DEMARK`

.. code-block:: console

    [jacob@moku ~]$ grep '^HAMLET.*DENMARK$' hamlet.txt 
    HAMLET, PRINCE OF DENMARK


Ever wonder how many lines in hamlet contain eight l's in them?

.. code-block:: console

    [jacob@moku ~]$ grep 'l.*l.*l.*l.*l.*l.*l.*l' hamlet.txt 
        Till then sit still, my soul. Foul deeds will rise,
        all welcome. We'll e'en to't like French falconers, fly at
        married already- all but one- shall live; the rest shall keep as
      Clown. I like thy wit well, in good faith. The gallows does well.

Man Pages
---------

Unix documentation is typically stored in man pages acces by the *man* command.
Try typing *man cat* into the console to see the manual page for the *cat* command.
Note, man pages are notoriously terse, technical, and often confusing to new users, so
while learning it may be better to ask google instead, but if all you want is to know 
optional command arguments the man page is the first place to look.

Exercise
--------
Make a directory in your home folder named *spam* containing subfolders *eggs*, *bacon*, *foo* and *bar* and then remove *spam/foo* and *spam/bar*
