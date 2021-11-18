#!/bin/bash
db=$1
shift
for var in "$@"
do
    sqlite3 $db -cmd ".headers on" -cmd ".mode column" -cmd ".print $var Attributes" ".print ------------------------------------------------------" "pragma table_info($var)" ".print " -cmd ".quit"

done

