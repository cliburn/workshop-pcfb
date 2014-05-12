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

## write the data to a file (either by pickle or csv+pickle)
outFilePath = os.path.join(".","excercise-np.pickle")
tmp = open(outFilePath,'w')
pickle.dump({'genes':geneList,'expList':expListIDs,'matrix':exprMat},tmp)
tmp.close()

tmp = open(outFilePath,'r')
resultsDict = pickle.load(tmp)
tmp.close()

## print out info
print ".............."
print "matrix of size (%s,%s)  created..."%(resultsDict['matrix'].shape)
print "gene list size - %s"%resultsDict['genes'].size
print "exp list size  - %s"%resultsDict['expList'].size
print ".............."
