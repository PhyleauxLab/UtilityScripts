#!/usr/bin/env python

from Bio import AlignIO
from Bio import Alphabet
import os
import sys

i = sys.argv[1]

input_handle = open(i,'r')
align = AlignIO.read(input_handle,"fasta",alphabet=Alphabet.IUPAC.IUPACAmbiguousDNA())
AlignIO.write(align,i.replace(".fasta",".nex"),"nexus")
