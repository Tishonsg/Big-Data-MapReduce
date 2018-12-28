#!/usr/bin/python

import sys
from itertools import *


''' VARIABLES '''
# SONG INFORMATION
song_lp_id = 3;
# Variable to ensure blank lines are not processed
min_len = 0;
# User adjustable parameter for k-skip
k_skip = 2


for line in sys.stdin:
    grams = line.split()
    # Pre cautionary check to ensure that no blank lines are being printed
    if len(grams) > min_len:
        bigram_skip = list(zip(grams, grams[k_skip:]))
        for tuple in bigram_skip:
            print('%s\t%s' % (tuple, 1))
