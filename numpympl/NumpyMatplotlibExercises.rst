.. pcfb file, created by ARichards

======================
Matplotlib - exercises
======================

Yeast cell cycle data
_____________________


:download:`File download </data/cellcycle.txt>`

The data were originally downloaded from the 
`Yeast Cell Cycle Analysis Project Page <http://genome-www.stanford.edu/cellcycle/data/rawdata>`_.
These data [1] by Spellman and Sherlock have likely been used in over a hundred papers.

1. look at the file so you know what you are getting into (less,wc)
2. copy this script into an editor and lets go over it

.. code-block:: python

    #!/usr/bin/env python

    import csv,os,sys,pickle
    import numpy as np

    ## read the file once to get numRows and numCols
    txtFilePath = os.path.join("..","data","cellcycle.txt")
    numRows = 0
    reader = csv.reader(open(txtFilePath, 'r'),delimiter='\t')
    expListIDs = reader.next()
    expListIDs = np.array(expListIDs[1:])
    for linja in reader:
        numRows+=1

    ## populate a matrix and name vectors with file info
    numColumns = len(expListIDs)
    exprMat = np.zeros([numRows,numColumns])
    reader = csv.reader(open(txtFilePath, 'r'),delimiter='\t')
    header = reader.next()
    rowInd = 0
    geneList = []

    for linja in reader:
        row = np.array(linja[1:])
        newRow = np.zeros(len(row),)
        nanInds = np.where(row == '')
        goodInds = np.where(row != '')
        newRow[nanInds] = np.nan
        newRow[goodInds] = [float(element) for element in row[goodInds]]
        exprMat[rowInd,:] = newRow
        rowInd +=1
        geneList.append(linja[0])
    geneList = np.array(geneList)

    ## print out info 
    print ".............."
    print "matrix of size (%s,%s)  created..."%(exprMat.shape)
    print "gene list size - %s"%geneList.size
    print "exp list size  - %s"%expListIDs.size
    print ".............."

    ## write the data to a file  
    outFilePath = os.path.join(".","excercise-np.pickle")
    tmp = open(outFilePath,'w')
    pickle.dump([geneList,expListIDs,exprMat],tmp)
    tmp.close()

3. save the file using your editor to a directory and use it to read cellcycle.txt.
   To do this you will need to change at least one line?
   
4. create your own script(s) that does the following
   
    * opens the pickle file 
    * calculates mean expression value for a gene
    * plot expression values for a given gene in a histogram
    * [extra] for a given gene create a lineplot that shows expression values for all the conditions
    * [extra] make plot that has boxplots for the 5 genes with the greatest expression mean
    * [extra] create a scatter plot (1 condition) where the negative expression values are green and positive ones are red

Note that:

>>> a = np.array([1,2,3,np.nan])
>>> a.max()
nan
>>> a.min()
nan
>>> a.mean()
nan
>>> np.where(np.isnan(a)==False)[0]
array([0, 1, 2])

Also, note that we do not transform, normalize or otherwise process the data in this example.  We are using this data set 
as a learning tool.  The missing data difficulties that arise are common in the biological sciences.


Bibliographic notes
___________________

1. Spellman P T, Sherlock, G, Zhang, M Q, Iyer, V R, Anders, K, Eisen, M B, Brown, P O, Botstein, D, Futcher, B.
Comprehensive identification of cell cycle-regulated genes of the yeast Saccharomyces cerevisiae by microarray hybridization.
*Molecular biology of the cell*, Vol. 9 (12): 3273-97, 1998. `PubMed <http://www.ncbi.nlm.nih.gov/pubmed/9843569>`_.
  
