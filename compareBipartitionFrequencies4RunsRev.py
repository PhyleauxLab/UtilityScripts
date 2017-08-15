#! /usr/bin/env python

import dendropy  # dendropy 4
import sys

### python compareBipartitionFrequenciesGGM.py "locusName" > outFile.tsv

def rbTreesList(inFilePath,fileNum,dpTaxonNamespace):
	with open(inFilePath, 'r') as inFile:
		per_row = []
		for line in inFile:
			per_row.append(line.strip().split('\t'))
		per_column = zip(*per_row)
	dpTrees = dendropy.TreeList()
	for tree in per_column[4][1:]:
		if fileNum == 1:
			nuTree = dendropy.Tree.get(data=tree, schema='newick')
		else:
			nuTree = dendropy.Tree.get(data=tree, schema='newick', taxon_namespace=dpTaxonNamespace)
		dpTrees.append(nuTree)
	return dpTrees

locus=sys.argv[1]
# Add first file
x=locus+'_posterior_run_1.trees'
fnum=1
dptaxa='NA'
r1Trees=rbTreesList(x,fnum,dptaxa)
# Add other runs, pass taxon namespace
fnum=2
dptaxa=r1Trees.taxon_namespace
y=locus+'_posterior_run_2.trees'
w=locus+'_posterior_run_3.trees'
z=locus+'_posterior_run_4.trees'
r2Trees=rbTreesList(y,fnum,dptaxa)
r3Trees=rbTreesList(w,fnum,dptaxa)
r4Trees=rbTreesList(z,fnum,dptaxa)

# get count of frequency of splits. 
# give dictionary of random # to represent split: decimal of how often it occurs in treeset.
r1sf = r1Trees.split_distribution().calc_freqs()
r2sf = r2Trees.split_distribution().calc_freqs()
r3sf = r3Trees.split_distribution().calc_freqs()
r4sf = r4Trees.split_distribution().calc_freqs()

# Get list of unique split IDs
sfDicts = [r1sf,r2sf,r3sf,r4sf]
sfUnique = []
for d in sfDicts:
	for key in d:
		if key not in sfUnique:
			sfUnique.append(key)

# Create dictionary with split ID as key, and list of frequencies for each run
allSplitFreqs = {}
for split in sfUnique:
	freqList=[]
	for d in sfDicts:
		if split in d:
			freqList.append(d[split])
		else:
			freqList.append(0.0)
	allSplitFreqs[split]=freqList


# print out dictionary of split ID and list of frequencies
# could use join function
for sp in allSplitFreqs:
	print(str(sp)+"	"+str(allSplitFreqs[sp][0])+"	"+str(allSplitFreqs[sp][1])+"	"+str(allSplitFreqs[sp][2])+"	"+str(allSplitFreqs[sp][3]))



