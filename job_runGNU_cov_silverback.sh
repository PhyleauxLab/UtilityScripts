#!/bin/bash
runName="numTips"
date="Aug3"

WDIR="/home/gmount/TreeScaper/$runName"
cd $WDIR

# Workers per node
WPN=6

# File list to pipe into task file
FILES="$WDIR/nexTrees_$runName.txt"

# File with one line task
TASK="$WDIR/pythonTask_cov_$runName.sh"

# Set up parallel call
# set log file, pass workers, whatever nodefile is, and working directory
PARALLEL="parallel --timeout 300% --joblog $runName_$date_cov.log -j $PBS_NODEFILE --wd $WDIR"

# Now call parallel and pass files and task. 
# This call with the {/} cuts the path off of the .nex file from the $FILES file
$PARALLEL -a $FILES sh $TASK {/} 
