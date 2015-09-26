# python count-stdin.py < small-01.csv

import sys

count = 0
for line in sys.stdin:
    count += 1

print count, 'lines in standard input'
