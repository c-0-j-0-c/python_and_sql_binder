#!/bin/bash
db=$1
shift
for var in "$@"
do
sqlite3 $db -cmd ".headers off" -cmd ".mode list" -cmd ".print $var: " "SELECT name FROM pragma_table_info('$var');" ".print " -cmd ".quit" > other.txt
tr -s '\n' ' ' < other.txt > output.txt
python Tables.py output.txt
echo ""
done
