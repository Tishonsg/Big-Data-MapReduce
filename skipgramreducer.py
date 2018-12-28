#!/usr/bin/python3
import sys


'''VARIABLES'''
min_len = 1
previous = None
ttl_freq = 0


# Redirect output from stdout to text file
# Not necessary for HDFS
# output = sys.stdout
# file = open('skipgrams.txt', 'w')
# sys.stdout = file

# Loop through n-grams of song lyrics and identify frequency of occurrences
for bigrams in sys.stdin:
    # Split key value pair into separate entities
    ngram,freq = bigrams.split('\t')

    # convert key (currently a string) to int
    try:
        freq = int(freq)
    except ValueError:
        continue

    # Incrementally increase freq of duplicate bigrams
    if ngram != previous:
        # Base case condition
        if previous is not None:
            print(previous + '\t' + str(ttl_freq))
        previous = ngram
    ttl_freq = ttl_freq + freq

print(previous + '\t' + str(ttl_freq))