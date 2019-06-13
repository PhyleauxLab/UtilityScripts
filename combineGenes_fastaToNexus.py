from Bio import Alphabet
from Bio.Nexus import Nexus
from Bio import SeqIO
import sys

# Expected arguments: (1) output file name, (2)-(N) input fasta files

print("Converting fasta files to nexus...")
print("")

nexusFiles = []

for fastaIn in sys.argv[2:]:
	print(fastaIn)
	SeqIO.convert(fastaIn, "fasta", fastaIn.replace(".fasta",".nex"), "nexus",alphabet=Alphabet.IUPAC.IUPACAmbiguousDNA())
	nexusFiles.append(fastaIn.replace(".fasta",".nex"))	

print("Concatenating alignments...")

nexusFileHandles = []

for nex in nexusFiles:
	nexusFileHandles.append(open(nex,'r'))

concatenate = Nexus.combine([(i.name,Nexus.Nexus(i)) for i in nexusFileHandles])
concatenate.write_nexus_data(filename=sys.argv[1])
	
