#!/usr/bin/env python

from Bio.Nexus import Nexus

gene1 = open('gene1.nex','r')	# For each gene you want to combine, change name of Nexus file.
gene2 = open('gene2.nex','r')

# Keep adding similar lines for the number of genes you want to combine

allGenes = (gene1,gene2) # Extend this tuple as needed

concatenate = Nexus.combine([(i.name,Nexus.Nexus(i)) for i in allGenes])
concatOutFile="outputFileName.nex"	# Change this to a meaningful output filename
concatenate.write_nexus_data(filename=concatOutFile)
