echo "# DAY 1 #"

cat data/day1.txt | awk '{ diff=$0-p; p=$0; if (NR > 1 && diff > 0) c++ } END {print c}'
echo "# t. 2"
cat data/day1.txt | awk '{ diff=$0-p4; p4=p3; p3=p2; p2=$0; if (NR > 3 && diff > 0) c++ } END {print c}'
echo " ------ "

