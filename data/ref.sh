#!/bin/bash

#Crunk xls files into pipe-delimited text files
OIFS="$IFS"

for f in *.xls
do
    BASE=${f%.xls}
    IFS='-' read -ra SPLIT <<< "$BASE"
    YEAR="${SPLIT[1]}"
    echo "Processing data for $YEAR ..."
    END=$(echo $(in2csv $f | awk '/Total,,,/ {print FNR}') - 1 | bc)
    START=$(echo $(in2csv $f | awk '/Placement City/ {print FNR}') + 1 | bc)
    in2csv $f | head -n $END | tail -n +$START | csvformat -D "|" > $BASE.txt
    fab parseCSV:"$YEAR","$BASE.txt","|"
    rm $BASE.txt
done

IFS="$OIFS"

#Stack 'em up
fab stackEmUp

#Pull out unique country names, match to dict with ISO 3-digit IDs, etc.
#Pull out unique states, match to dict with FIPS, etc.

