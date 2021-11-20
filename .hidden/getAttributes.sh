#!/bin/bash
db=$1
shift
for var in "$@"
do
    echo "$var Attributes^<TABLE>"
    sqlite3 $db -cmd ".headers on" -cmd ".mode html" "pragma table_info($var)" -cmd ".quit"
    echo "</TABLE>&"
done
