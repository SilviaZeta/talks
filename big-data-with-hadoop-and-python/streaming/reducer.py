#!/usr/bin/env python

import sys
from operator import itemgetter
from itertools import groupby

data = (line.rstrip().split('\t') for line in sys.stdin)
func = lambda x: x[0]

for word, counts in groupby(data, func):
    total = sum(int(c) for _, c in counts)
    print '%s\t%s' % (word, total)
