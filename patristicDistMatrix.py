#! /usr/bin/env python

# Calculates a patristic distance matrix between all leaves in a tree.
# The name of the tree file (nexus format) should be provided as the first argument.
# The name of the matrix output file should be provided as the second argument.
# Uses Dendropy 3

import dendropy
from dendropy import treecalc
import sys

tree = dendropy.Tree.get_from_path(sys.argv[1], "nexus",preserve_underscores=True)
pdm = treecalc.PatristicDistanceMatrix(tree)

matFile = open(sys.argv[2],'w')

matFile.write("\t")

for t in tree.taxon_set:
	matFile.write("%s\t" % t.label,)

matFile.write('\n')

for i, t1 in enumerate(tree.taxon_set):
	matFile.write("%s\t" % t1.label,)
	matFile.write('\t' * (i+1),)
	for t2 in tree.taxon_set[i+1:]:
		matFile.write("%s\t" % pdm(t1,t2))
	matFile.write('\n')

matFile.close()
