cat data/day2.input.txt | awk '$1=="forward" { h+=$2; d+=a*$2 } $1=="up" { a-=$2 } $1=="down" { a+=$2 } END { print h*d }'
