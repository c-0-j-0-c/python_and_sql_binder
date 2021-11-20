#!/bin/bash
db=$1
shift
for var in "$@"
do
sqlite3 $db -cmd ".headers off" -cmd ".mode list" -cmd ".print $var: " "SELECT name FROM pragma_table_info('$var');" ".print " -cmd ".quit" > ./.hidden/other.txt
tr -s '\n' ' ' < ./.hidden/other.txt > ./.hidden/output.txt
python ./.hidden/Tables.py ./.hidden/output.txt
echo ""
done
