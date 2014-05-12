Data management and relational databases
========================================


The (very) Basics of SQL
------------------------
Databases are a very large and complex topic.  Classes typically cover weeks, so in our short time
we will only scratch the surface of the basics of selecting, inserting, and joining selects.

Data in relational databases are organized into tables, containing fixed columns of specified 
data types. For our example we will use two tables, people and experiment, described below.

.. code-block:: sqlite3

   create table people (
            id integer primary key,
      name varchar, 
      position varchar,
      phone varchar,
      office varchar
   );
   
   create table experiment (
      id integer primary key,
      name varchar,
      researcher integer,
      description text,
      foreign key(researcher) references people(id)
   );


Select
^^^^^^

the select command retrieves data from the database. 

.. code-block:: sqlite3

   sqlite> select * from people;
   0|Alice|Research Director|555-123-0001|4b
   1|Bob|Research assistant|555-123-0002|17
   2|Charles|Research assistant|555-123-0001|24
   3|David|Research assistant|555-123-0001|8
   
   sqlite> select * from experiment;
   0|EBV Vaccine trial|0|A vaccine trial
   1|Flu antibody study|2|Study of the morphology of flu antibodies
   

The * in the *select* statement says to select all columns.  If you only need a few of the columns
you can select them by name.

.. code-block:: sqlite3

   sqlite> select name, phone from people;
   Alice|555-123-0001
   Bob|555-123-0002
   Charles|555-123-0001
   David|555-123-0001
   
   sqlite> select name, description from experiment;
   EBV Vaccine trial|A vaccine trial
   Flu antibody study|Study of the morphology of flu antibodies
   
You can also limit the returned results to rows that match specified information using the *where*
directive.

.. code-block:: sqlite3

   sqlite> select * from people where name == 'Alice';
   0|Alice|Research Director|555-123-0001|4b
   
   sqlite> select position from people where name == 'David';
   Research assistant
   


Insert
^^^^^^
Adding values to the database is done by using the *insert* statement.

.. code-block:: sqlite3

   sqlite> insert into people values ( Null, 'Edward', 'Toadie', 'None', 'Basement');
   sqlite> select * from people where name == 'Edward';
   4|Edward|Toadie|None|Basement

Update
^^^^^^

You can also change existing rows once they've been inserted.  *update* takes a table name
as it's first argument followed by *set* column = value. With out a where clause this will
set all row's values.  You there for will almost always use the where clause so that you get
specific row/rows values updated.

.. code-block:: sqlite3

   sqlite> select * from people;
   0|Alice|Research Director|555-123-0001|4b
   1|Bob|Research assistant|555-123-0002|17
   2|Charles|Research assistant|555-123-0001|24
   3|David|Research assistant|555-123-0001|8
   4|Edward|Toadie|None|Basement
   sqlite> update people set name='Eddie' where id=4;
   sqlite> select * from people;
   0|Alice|Research Director|555-123-0001|4b
   1|Bob|Research assistant|555-123-0002|17
   2|Charles|Research assistant|555-123-0001|24
   3|David|Research assistant|555-123-0001|8
   4|Eddie|Toadie|None|Basement

Delete
^^^^^^

Similar to updating you can *delete* rows from the database.  The argument again will
most likely want a where clause to prevent deleting all rows in a table.

.. code-block:: sqlite3

   sqlite> select * from people;
   0|Alice|Research Director|555-123-0001|4b
   1|Bob|Research assistant|555-123-0002|17
   2|Charles|Research assistant|555-123-0001|24
   3|David|Research assistant|555-123-0001|8
   4|Eddie|Toadie|None|Basement
   sqlite> delete from people where name='Eddie';
   sqlite> select * from people;
   0|Alice|Research Director|555-123-0001|4b
   1|Bob|Research assistant|555-123-0002|17
   2|Charles|Research assistant|555-123-0001|24
   3|David|Research assistant|555-123-0001|8


Joins
^^^^^

The power of relational databases lies in recording relations (the foreign key in 
the table declaration).  To join two tables you use the *join* keyword in the
select statement and provide a relation to join the two tables. Note, that since 
both the people and experiment tables have a column called name we must cast the
tables using the as statement.

.. code-block:: sqlite3

   sqlite> select p.name, e.name from people as p join experiment as e where e.researcher == p.id;
   Alice|EPV Vaccine trial
   Charles|Flu antibody study


Python and DBI
--------------

Working with relational databases is fairly simple with python, 
 1. Create a connection object
 2. Execute a SQL statement
 3. Iterate over results

.. code-block:: ipython

   In [1]: import sqlite3
   
   In [2]: con = sqlite3.connect('pcfb.sqlite')
   
   In [3]: r = con.execute('select * from people')
   
   In [4]: for i in r:
      ...:    print i
    
   (0, u'Alice', u'Research Director', u'555-123-0001', u'4b')
   (1, u'Bob', u'Research assistant', u'555-123-0002', u'17')
   (2, u'Charles', u'Research assistant', u'555-123-0001', u'24')
   (3, u'David', u'Research assistant', u'555-123-0001', u'8')
   (4, u'Edward', u'Toadie', u'None', u'Basement')

   In [5]: r = con.execute('select p.name, e.name from people as p join experiment as e where e.researcher == p.id')

   In [6]: for i in r:
      ...:     print 'Name: %s\n\tExperiment: %s' % (i[0],i[1])
      ...: 
   Name: Alice
      Experiment: EPV Vaccine trial
   Name: Charles
      Experiment: Flu antibody study
   
   
Exercise:
---------

Write a script to a add a new user and experiment to the database, remove Alice, and reassign her experiments to the new user.  Then have it print out all the experiment names with who owns each experiment.
