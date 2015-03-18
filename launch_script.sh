#!/bin/bash
#script de lancement du calcul de pi en parallèle

machines=`cat $OAR_FILE_NODES`
nb_machines=`wc -l $OAR_FILE_NODES`
i=0
max=1000000

for m in $machines;do
    oarsh $m echo `python3 part_of_pi.py $i $nb_machines $max > result_tmp` &
    $i=$i + 1
done