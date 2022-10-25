#!/usr/bin/env python3
import sys

def reduce():
    s = 0
    counter = 0
    for line in sys.stdin:
        vals = line.strip().split("\t")
        s += float(vals[0])
        counter += 1

    sys.stdout.write("{}\n".format(s / counter))
            
            
if __name__ == "__main__":
    reduce()
