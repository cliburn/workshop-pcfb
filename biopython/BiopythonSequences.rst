.. pcfb file, created by ARichards

===================================
Biopython - sequences and alphabets
===================================

The Sequence object
-------------------

Some examples will also require a working internet connection in order to run.  

>>> from Bio.Seq import Seq
>>> from Bio.Alphabet import IUPAC
>>> my_seq = Seq("AGTACACTGGT", IUPAC.unambiguous_dna)
>>> my_seq
Seq('AGTACACTGGT', IUPACUnambiguousDNA())
>>> my_seq.alphabet
IUPACUnambiguousDNA()

A *Seq* object in python acts like a normal python string.
             
>>> for letter in my_seq:
...     print letter
>>> len(my_seq)
>>> my_seq[4:12]
>>> my_seq[::-1]
>>> str(my_seq)

Nucleotide counts, transcription, translation
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

>>> my_seq.count("A")
3

to get the GC nucleotide content.

>>> from Bio.SeqUtils import GC
>>> GC(my_seq)
45.45454545454545

transcription and translation

>>> my_mRNA = my_seq.transcribe()
Seq('AGUACACUGGU', IUPACUnambiguousRNA())
>>> my_seq.translate()
Seq('STL', IUPACProtein())

complement and reverse complement

>>> str(my_seq)
'AGTACACTGGT'
>>> my_seq.complement()
Seq('TCATGTGACCA', IUPACUnambiguousDNA())
>>> my_seq.reverse_complement()
Seq('ACCAGTGTACT', IUPACUnambiguousDNA())


You can translate directly from the DNA coding sequence or you can use the mRNA directly.

>>> from Bio.Seq import Seq
>>> from Bio.Alphabet import IUPAC
>>> messenger_rna = Seq("AUGGCCAUUGUAAUGGGCCGCUGAAAGGGUGCCCGAUAG", IUPAC.unambiguous_rna)
>>> messenger_rna
Seq('AUGGCCAUUGUAAUGGGCCGCUGAAAGGGUGCCCGAUAG', IUPACUnambiguousRNA())
>>> messenger_rna.translate()
Seq('MAIVMGR*KGAR*', HasStopCodon(IUPACProtein(), '*'))

Now, you may want to translate the nucleotides up to the first in frame stop codon, and then stop (as happens in nature):

>>> coding_dna.translate()
Seq('MAIVMGR*KGAR*', HasStopCodon(IUPACProtein(), '*'))
>>> coding_dna.translate(to_stop=True)
Seq('MAIVMGR', IUPACProtein())

.. admonition:: Exercise

    1. There is so much stuff available in biopython.  What happens if you do this?
    
       >>> from Bio.Data import CodonTable
       >>> standard_table = CodonTable.unambiguous_dna_by_id[1]
       >>> mito_table = CodonTable.unambiguous_dna_by_id[2]
       >>> print standard_table
       >>> print mito_table

The Sequence record object
--------------------------

The *SeqRecord* objects are the basic data type for the *SeqIO* objects and they are very similar to *Seq* objects,however,
there are a few additional attributes.

    * **seq**  - The sequence itself, typically a Seq object.
    * **id**    - The primary ID used to identify the sequence – a string. In most cases this is something like an accession number.
    * **name** - A 'common' name/id for the sequence – a string. In some cases this will be the same as the accession number, but it could also be a clone name. Analagous to the LOCUS id in a GenBank record.
    * **description** - A human readable description or expressive name for the sequence – a string.

We can think of the *SeqRecord* as a container that has the above attributes including the *Seq*.

.. admonition:: Exercise

    1. Copy the following script into an editor and save as 'BioSequences.py'
    2. Open a terminal window and cd into the appropriate directory.
    3. Fill in the missing lines with code

.. code-block:: python

    from Bio.Seq import Seq
    from Bio.SeqRecord import SeqRecord

    ## create a simple SeqRecord object
    simple_seq = Seq("GATCAGGATTAGGCC")
    simple_seq_r = SeqRecord(simple_seq)
    simple_seq_r.id = "AC12345"
    simple_seq_r.description = "I am not a real sequence"

    ## print summary
    print simple_seq_r.id
    print simple_seq_r.description
    print str(simple_seq_r.seq)
    print simple_seq_r.seq.alphabet

    ## translate the sequence
    translated_seq = simple_seq_r.seq.translate()
    print translated_seq

    # exercise 1 -- translate the sequence only until the stop codon


    # exercise 2 -- get the reverse complement of the sequence


    # exercise 3 -- get the reverse of the sequence (just like for lists)


    # exercise 4 -- get the GC nucleotide content 


The Sequence IO object
----------------------

There is one more object that we have to discuss and this the *SeqIO* object is like a container for multiple *SeqRecord* objects.

.. code-block:: python

    import os
    from Bio import SeqIO

    '''
    We use a list here to save the gene records from a FASTA file
    If you have many records a dictionary will make the program faster.
    
    '''

    ## save the sequence records to a list
    allSeqRecords = []
    allSeqIDs     = []
    pathToFile = os.path.join("..","data","ls_orchid.fasta")
    for seq_record in SeqIO.parse(pathToFile, "fasta"):
	allSeqRecords.append(seq_record)
	allSeqIDs.append(seq_record.id.split("|")[1])
	print seq_record.id
	print str(seq_record.seq)
	print len(seq_record)

    ## print out fun stuff about the sequences
    print "We found ", len(allSeqIDs), "sequences"
    print "information on the third sequence:"
    ind = 2
    seqRec = allSeqRecords[ind]
    print "\t", "GI number     ", allSeqIDs[ind]
    print "\t", "full id       ", seqRec.id
    print "\t", "num nucleo.   ", len(seqRec.seq)
    print "\t", "1st 10 nucleo.", seqRec.seq[:10]


Just as easy as it is to read a set of files we can save modified versions (i.e. QA). Also, it is almost the exact same 
code as above to parse sequences from a GenBank (.gb) file.

There is really way to much to cover in the time we have, but if you have Next Generation Sequencing data then refer
to sections 4.8, 16.1.7 and 16.1.8 of the `biopython tutorial <http://biopython.org/DIST/docs/tutorial/Tutorial.html>`_.
There is even support for binary formats (i.e. `SFF <http://biopython.org/DIST/docs/api/Bio.SeqIO.SffIO-module.html>`_).
