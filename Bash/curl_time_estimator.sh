#!/bin/bash
name=www.stanford.edu
N=100
unit=' ms'
for((i=1; i<$N; i++))
do
curl -o /dev/null -s -w "%{time_total}\n" $name >> $name.txt
done
sed "s/,/./g" "$name".txt>>"$name".log #per sostituire le virgole dello stupido curl con dei punti
awk -v N=1 '{sum+=$N} END {if(NR>0) printf sum*1000/NR}' "$name".log
echo $unit
