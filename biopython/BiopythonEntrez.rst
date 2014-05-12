.. pcfb file, created by ARichards

============================
Biopython - Entrez databases
============================

NCBI's Guidelines
-----------------

Taken from the `tutorial <http://biopython.org/DIST/docs/tutorial/Tutorial.html#htoc33>`_.

Before using Biopython to access the NCBI’s online resources (via Bio.Entrez or some of the other modules), please read the NCBI’s Entrez User Requirements. 
If the NCBI finds you are abusing their systems, they can and will ban your access!

To paraphrase:
For any series of more than 100 requests, do this at weekends or outside USA peak times. This is up to you to obey.
Use the `http://eutils.ncbi.nlm.nih.gov <http://eutils.ncbi.nlm.nih.gov>`_ address, not the standard NCBI Web address. Biopython uses this web address.
Make no more than three requests every seconds (relaxed from at most one request every three seconds in early 2009). This is automatically enforced by Biopython.
Use the optional email parameter so the NCBI can contact you if there is a problem. You can either explicitly set this as a parameter with each call to Entrez (e.g. include email="A.N.Other@example.com" in the argument list), or as of Biopython 1.48, you can set a global email address:

>>> from Bio import Entrez
>>> Entrez.email = "A.N.Other@example.com"

Bio.Entrez will then use this email address with each call to Entrez. The example.com address is a reserved domain name specifically for documentation (RFC 2606). Please DO NOT use a random email – it’s better not to give an email at all. The email parameter will be mandatory from June 1, 2010. In case of excessive usage, NCBI will attempt to contact a user at the e-mail address provided prior to blocking access to the E-utilities.

If you are using Biopython within some larger software suite, use the tool parameter to specify this. You can either explicitly set the tool name as a parameter with each call to Entrez (e.g. include tool="MyLocalScript" in the argument list), or as of Biopython 1.54, you can set a global tool name:

>>> from Bio import Entrez
>>> Entrez.tool = "MyLocalScript"

The tool parameter will default to Biopython.
For large queries, the NCBI also recommend using their session history feature (the WebEnv session cookie string, see Section 8.15). This is only slightly more complicated. 


What databases do I have access to?
___________________________________

>>> from Bio import Entrez
>>> Entrez.email = "adam.richards@stat.duke.edu"
>>> handle = Entrez.einfo()
>>> record = Entrez.read(handle)
>>> record["DbList"]
['pubmed', 'protein', 'nuccore', 'nucleotide', 'nucgss', 'nucest', 'structure', 'genome', 
'genomeprj', 'bioproject', 'biosample', 'biosystems', 'blastdbinfo', 'books', 'cdd', 'clone', 
'gap', 'gapplus', 'dbvar', 'epigenomics', 'gene', 'gds', 'geo', 'geoprofiles', 'homologene', 
'journals', 'mesh', 'ncbisearch', 'nlmcatalog', 'omia', 'omim', 'pmc', 'popset', 'probe', 
'proteinclusters', 'pcassay', 'pccompound', 'pcsubstance', 'pubmedhealth', 'seqannot', 'snp', 
'sra', 'taxonomy', 'toolkit', 'toolkitall', 'unigene', 'unists', 'gencoll', 'gcassembly', 
'assembly']


What if I want info about a database?
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

>>> handle = Entrez.einfo(db="pubmed")
>>> record = Entrez.read(handle)
>>> record["DbInfo"]["Description"]
'PubMed bibliographic record'
>>> record["DbInfo"]["Count"]
'21827335'


How do I search a db for a given term?
______________________________________

>>> handle = Entrez.esearch(db="pubmed", term="biopython")
>>> record = Entrez.read(handle)
>>> record["IdList"]
['22399473', '21666252', '21210977', '20015970', '19811691', '19773334', '19304878', 
'18606172', '21585724', '16403221', '16377612', '14871861', '14630660', '12230038']


Other databases?
^^^^^^^^^^^^^^^^

>>> handle = Entrez.esearch(db="nucleotide",term="Cypripedioideae[Orgn] AND matK[Gene]")
>>> record = Entrez.read(handle)
>>> record["Count"]
'75'

Get all journals that have 'computational' as a term
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

>>> handle = Entrez.esearch(db="journals", term="computational")
>>> record = Entrez.read(handle)
>>> record["Count"]
'54'
>>> record["IdList"]
['39206', '37505', '37511', '37435', '37518', '36366', '39786', '34878', '30367', '38517', '33843', '37406', '40084', '36622', '39212', '33823', '32989', '33190', '38518', '40055']

Ok I have a term now I want the item itself
___________________________________________

>>> from Bio import Entrez, SeqIO
>>> handle = Entrez.efetch(db="nucleotide", id="186972394",rettype="gb", retmode="text")
>>> record = SeqIO.read(handle, "genbank")
>>> handle.close()
>>> print record
ID: EU490707.1
Name: EU490707
Description: Selenipedium aequinoctiale maturase K (matK) gene, partial cds; chloroplast.
Number of features: 3
/sequence_version=1
/source=chloroplast Selenipedium aequinoctiale
/taxonomy=['Eukaryota', 'Viridiplantae', 'Streptophyta', 'Embryophyta', 'Tracheophyta', 'Spermatophyta', 'Magnoliophyta', 'Liliopsida', 'Asparagales', 'Orchidaceae', 'Cypripedioideae', 'Selenipedium']
/keywords=['']
/references=[Reference(title='Phylogenetic utility of ycf1 in orchids: a plastid gene more variable than matK', ...), Reference(title='Direct Submission', ...)]
/accessions=['EU490707']
/data_file_division=PLN
/date=15-JAN-2009
/organism=Selenipedium aequinoctiale
/gi=186972394
Seq('ATTTTTTACGAACCTGTGGAAATTTTTGGTTATGACAATAAATCTAGTTTAGTA...GAA', IUPACAmbiguousDNA())


>>> handle = Entrez.efetch(db="pubmed", id="21210977")
>>> print handle.read()



