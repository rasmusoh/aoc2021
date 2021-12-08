echo "# DAY 2 #"

cat data/day2.txt | awk '$1=="forward" { h+=$2 } $1=="up" { d-=$2 } $1=="down" { d+=$2 } END { print h*d }'
echo "# t. 2"
cat data/day2.txt | awk '$1=="forward" { h+=$2; d+=a*$2 } $1=="up" { a-=$2 } $1=="down" { a+=$2 } END { print h*d }'
echo " ------ "
