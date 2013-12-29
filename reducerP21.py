#!/usr/bin/python

import sys

hitTotal = 0
oldKey = None

# Loop around the data
# It will be in the format key\tval
# Where key is the store name, val is the Hit amount
#
# All the hit for a particular store will be presented,
# then the key will change and we'll be dealing with the next store

for line in sys.stdin:
    data_mapped = line.strip().split("\t")
    if len(data_mapped) != 2:
        # Something has gone wrong. Skip this line.
        continue

    thisKey, thisHit = data_mapped

    if oldKey and oldKey != thisKey:
        print oldKey, "\t", hitTotal
        oldKey = thisKey;
        hitTotal = 0

    oldKey = thisKey
    hitTotal += int(thisHit)

if oldKey != None:
    print oldKey, "\t", hitTotal

