#!/bin/sh
#
#Script to test while statement
#
#

#if [ $# -eq 0 ]
#then
#   echo "Error - Number missing form command line argument"
#   echo "Syntax : $0 number"
#   echo " Use to print multiplication table for given number"
#exit 1
#fi
#n=$1
n=0
i=1
while [ $i -le 10000 ]
do
  echo "[s] Sample output is  $i"
  i=`expr $i + 1`
  sleep 1
done
