#!/usr/bin/env python3
import sys


def reduce():
    K = Ex = Ex2 = 0.0
    n = 0

    for line in sys.stdin:
        vals = line.strip().split("\t")

        if n == 0:
            K = float(vals[0])
        n += 1
        Ex += float(vals[0]) - K
        Ex2 += (float(vals[0]) - K) ** 2

    sys.stdout.write(f'{((Ex2 - Ex**2 / n) / (n - 1)) ** (1/2)}\n')
            
            
if __name__ == "__main__":
    reduce()
