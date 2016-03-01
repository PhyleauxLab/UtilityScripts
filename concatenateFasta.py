from Bio import SeqIO
import glob



##########################################################################################
##  Concatenates alignments from multiple fasta files into a single new file.
##  
##  Expects a directory of alignments in fasta format, with each individual sequence 
##    being named exactly the same thing in each file. 
##
##  Script will concatenate the sequences, keep track of the order, and write out a new
##    fasta file with concatenated sequences. Will also produce a text file with a list 
##    of file names and the length of the sequences in those files.
##
##  Requirements:
##  
##   1. Python 2.7
##   2. Biopython
##########################################################################################


inDir = '' ## directory where alignments are located
outSeqFile = '' ## name of new concatenated fasta file
outLengthFile = '' ## name of length csv file



alignmentFiles = glob.glob(inDir + '*')
allsequences = {}
alllengths = []
order = []
sequences = SeqIO.parse(open(alignmentFiles[0], 'r'), 'fasta') 
for s in sequences :
	order.append(s.id.strip())
	allsequences[s.id] = ''

for a in alignmentFiles :
    sequences = SeqIO.parse(open(a, 'r'), 'fasta')
    for s in sequences :
        for o in order :
            if o == s.id.strip() :
                allsequences[s.id] = allsequences[s.id] + s.seq
    
    alllengths.append(str(len(s.seq)))


outHandle = open(outSeqFile, 'w')
outHandle2 = open(outLengthFile, 'w')
for o in order :
    outStr = ">" + o + "\n" + str(allsequences[o]) + "\n"
    outHandle.write(outStr)

for l, a in zip(alllengths, alignmentFiles) :
    outHandle2.write(l + "\t" +  a + "\n")
