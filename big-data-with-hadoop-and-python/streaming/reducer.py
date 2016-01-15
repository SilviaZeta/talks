#!/usr/bin/env python

import sys
from itertools import groupby

data = (line.rstrip().split('\t') for line in sys.stdin)

for word, counts in groupby(data, lambda x: x[0]):
    total = sum(int(c) for _, c in counts)
    print '%s\t%s' % (word, total)
