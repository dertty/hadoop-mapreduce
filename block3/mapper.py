#!/usr/bin/env python3
import sys
import csv

def mapper():
    for line in csv.reader(sys.stdin):
        if len(line[9]) > 0 and line[9] != 'price':
            sys.stdout.write(f'{line[9]}\t1\n')

    # import pandas as pd
    # print(pd.read_csv('block3/AB_NYC_2019.csv')['price'].dropna().mean())
    # print(pd.read_csv('block3/AB_NYC_2019.csv')['price'].dropna().std())

if __name__ == "__main__":
    mapper()