#! /usr/bin/env python

"""
Written to work with Dendropy 4 and Python 2.7. 
Assumes default naming scheme from MrBayes 3.2.5.

Expected arguments: 
(1) Root file name
(2) Burn-in
(3) Number of runs to combine
(4) Subsampling interval
"""

import dendropy
import sys

rootName = sys.argv[1]
burn = int(sys.argv[2])
nRuns = int(sys.argv[3])

trees = dendropy.TreeList()

for rep in range(nRuns):

    trees.read_from_path("%s.run%d.t" % (rootName,rep+1),
                         schema="nexus",
                         tree_offset=burn,
                         preserve_underscores=True)
					 
print("Starting treelist length: %d" % len(trees))

subSampTrees = trees[1::int(sys.argv[4])]

print("Subsampled treelist length: %d" % len(subSampTrees))

treeCounter = 1
for tree in subSampTrees:
	tree._set_label("%s_tree_%d" % (rootName,treeCounter))
	treeCounter = treeCounter + 1

subSampTrees.write(path="%s.treeList.nex" % rootName,
                   schema="nexus",
                   # suppress_taxa_blocks=True,
                   translate_tree_taxa=True,
                   unquoted_underscores=True)
