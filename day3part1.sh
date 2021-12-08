echo "# DAY 3 #"
cat data/day3.txt | awk  -F '' '{ for (i=1;i<=NF;i++) {cs[i]+= ($i == 1 ? 1: -1)}} END { printf " ibase=2;"; for (pos in cs) { printf (cs[pos] > 0 ? 1 : 0)} print ""; printf "ibase=2;"; for (pos in cs) { printf (cs[pos] < 0 ? 1 : 0) } print ""}' | bc | awk 'BEGIN {s=1} {s*=$1} END {print s}'
echo " ------ "
