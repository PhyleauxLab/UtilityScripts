#! /usr/bin/env python

import dendropy  # dendropy 4
import sys

# Reading in trees from two files specified as command-line arguments
r1Trees = dendropy.TreeList.get(path=sys.argv[1], schema='newick')
r2Trees = dendropy.TreeList.get(path=sys.argv[2], schema='newick', taxon_namespace=r1Trees.taxon_namespace)

# Set burnin
burnin = 1001

# Remove burnin and calculate frequencies for all splits in each tree set
r1sf = r1Trees[burnin:len(r1Trees)].split_distribution().calc_freqs()
r2sf = r2Trees[burnin:len(r2Trees)].split_distribution().calc_freqs()

# Create dictionary to hold split frequencies across tree sets
allSplitFreqs = {}

# Record split frequncies for all splits in the first tree set
for sp in r1sf:
	if sp in r2sf:		# Both tree sets have this split
		allSplitFreqs[sp] = [ r1sf[sp] , r2sf[sp] ]
	else:				# Only tree set 1 has this split
		allSplitFreqs[sp] = [ r1sf[sp] , 0.0 ]
		
for sp in r2sf:
	if sp not in allSplitFreqs:		# Only tree set 2 has these splits
		allSplitFreqs[sp] = [ 0.0 , r2sf[sp] ]
		
# Printing paired lists of split frequencies
for sp in allSplitFreqs:
	print(str(sp)+"	"+str(allSplitFreqs[sp][0])+"	"+str(allSplitFreqs[sp][1]))
