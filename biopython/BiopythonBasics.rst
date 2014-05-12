.. pcfb file, created by ARichards

==================
Biopython - basics
==================

Introduction
____________

From the `biopython website <http://www.biopython.org>`_ their goal is to 
"make it as easy as possible to use Python for bioinformatics by creating high-quality, reusable modules and scripts."
These modules use the `biopython tutorial <biopython.org/DIST/docs/tutorial/Tutorial.html>`_ as a template for what 
you will learn here.  Here is a list of some of the most common data formats in computational biology that are 
supported by biopython.

+-----------------------------------+-------------------------------------------------------------+
| Uses                              | Note                                                        |
+===================================+=============================================================+
| Blast                             | finds regions of local similarity between sequences         |
+-----------------------------------+-------------------------------------------------------------+
| ClustalW                          | multiple sequence alignment program                         |
+-----------------------------------+-------------------------------------------------------------+
| GenBank                           | NCBI sequence database                                      |
+-----------------------------------+-------------------------------------------------------------+
| PubMed and Medline                | Document database                                           |
+-----------------------------------+-------------------------------------------------------------+
| ExPASy                            | SIB resource portal (Enzyme and Prosite)                    |
+-----------------------------------+-------------------------------------------------------------+
| SCOP                              | Structural Classification of Proteins (e.g. 'dom','lin')    |
+-----------------------------------+-------------------------------------------------------------+
| UniGene                           | computationally identifies transcripts from the same locus  |
+-----------------------------------+-------------------------------------------------------------+
| SwissProt                         | annotated and non-redundant protein sequence database       |
+-----------------------------------+-------------------------------------------------------------+

Some of the other principal functions of biopython.

* A standard sequence class that deals with sequences, ids on sequences, and sequence features.
* Tools for performing common operations on sequences, such as translation, transcription and weight calculations.
* Code to perform classification of data using k Nearest Neighbors, Naive Bayes or Support Vector Machines.
* Code for dealing with alignments, including a standard way to create and deal with substitution matrices.
* Code making it easy to split up parallelizable tasks into separate processes.
* GUI-based programs to do basic sequence manipulations, translations, BLASTing, etc.

Getting started
_______________

>>> import Bio
>>> Bio.__version__
'1.58'

Some examples will also require a working internet connection in order to run.  

>>> from Bio.Seq import Seq
>>> my_seq = Seq("AGTACACTGGT")
>>> my_seq
Seq('AGTACACTGGT', Alphabet())
>>> aStringSeq = str(my_seq)
>>> aStringSeq
'AGTACACTGGT'
>>> my_seq_complement = my_seq.complement()
>>> my_seq_complement
Seq('TCATGTGACCA', Alphabet())
>>> my_seq_reverse = my_seq.reverse()
>>> my_seq_rc = my_seq.reverse_complement()
>>> my_seq_rc
Seq('ACCAGTGTACT', Alphabet())

There is so much more, but first before we get into it we should figure out how to 
get sequences in and out of python.

:download:`File download </data/ls_orchid.fasta>`

`FASTA <http://www.ncbi.nlm.nih.gov/BLAST/blastcgihelp.shtml>`_ formats are the standard format for storing 
sequence data.  Here is a little reminder about sequences.

+-------------------+---------------------+-------------------+---------------------------+
| Nucleic acid code | Note                | Nucleic acid code | Note                      |
+===================+=====================+===================+===========================+
| A                 | adenosine           | K                 | G/T (keto)                |
+-------------------+---------------------+-------------------+---------------------------+
| T                 | thymidine           | M                 | A/C (amino)               |
+-------------------+---------------------+-------------------+---------------------------+
| C                 | cytidine            | R                 | G/A (purine)              |
+-------------------+---------------------+-------------------+---------------------------+
| G                 | guanine             | S                 | G/C (strong)              |
+-------------------+---------------------+-------------------+---------------------------+
| N                 | A/G/C/T (any)       | W                 | A/T (weak)                | 
+-------------------+---------------------+-------------------+---------------------------+
| U                 | uridine             | B                 | G/T/C                     | 
+-------------------+---------------------+-------------------+---------------------------+
| D                 | G/A/T               | Y                 | T/C (pyrimidine)          | 
+-------------------+---------------------+-------------------+---------------------------+
| H                 | A/C/T               | V                 | G/C/A                     | 
+-------------------+---------------------+-------------------+---------------------------+

             
Here is quickly a bit about how biopython works with sequences

>>> for seq_record in SeqIO.parse(os.path.join("data","ls_orchid.fasta"), "fasta"):
...     print seq_record.id
...     print repr(seq_record.seq)
...     print len(seq_record)
... 
gi|2765658|emb|Z78533.1|CIZ78533
Seq('CGTAACAAGGTTTCCGTAGGTGAACCTGCGGAAGGATCATTGATGAGACCGTGG...CGC', SingleLetterAlphabet())
740
