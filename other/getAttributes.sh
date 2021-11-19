#!/bin/bash
db=$1
shift
for var in "$@"
do
    echo "<i>$var Attributes</i></br> <hr> <TABLE>"
    sqlite3 $db -cmd ".headers on" -cmd ".mode html" "pragma table_info($var)" -cmd ".quit"
    echo "</TABLE><hr>"
    echo ""
done

