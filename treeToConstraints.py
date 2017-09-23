#! /usr/bin/env python

# Takes an input tree and returns a list of constraints (one per bipartition)

from dendropy import Tree, TaxonSet
from cStringIO import StringIO
import sys

def main(argv):

	# Instantiates taxon set object for tree list
	taxa = TaxonSet()

	# Reads in tree string from the command line
	focalTree = Tree(stream=StringIO(argv[0]),schema="newick",rooted=False,taxon_set=taxa)

	# Iterates over all internal nodes in the focal tree (generating one constraint each)
	for i in focalTree.internal_nodes():
	
		# Defines a list that initially contains all the leaf nodes from focal tree
		fullTaxonSet = focalTree.leaf_nodes()
	
		# Iterates over all internal nodes that are not the root
		if i is not focalTree.seed_node:

			# Instantiates string (conTree) to hold the constraint tree string
			conTree = "(("

			# Iterates over leaf nodes that are descendants of the current internal node
			for j in i.leaf_nodes():
			
				# Appropriately adds the taxon name to the constraint tree string
				if j is i.leaf_nodes()[0]:
					conTree = conTree + str(j.taxon)
				else:
					conTree = conTree + "," + str(j.taxon)
					
			# Closes out the part of the constraint for taxa descended from the focal node
			conTree = conTree + ")"
			
			# Takes all leaves and removes those descended from the focal node
			for j in i.leaf_nodes():
				fullTaxonSet.remove(j)
				
			# Adds all leaves not descended from the focal node to the constraint tree string
			for j in fullTaxonSet:
					conTree = conTree + "," + str(j.taxon)
			
			# Closes constraint tree string
			conTree = conTree + ")"
			
			# Prints constraint tree string to the screen
			print conTree

if __name__ == "__main__":
	main(sys.argv[1:])
