#!/usr/bin/env python3

from Exercise02 import value_counts_efficient

def find_repeats_v1(counter):
    repeats = []
    for k,v in counter.items():
        if v > 1:
            repeats.append(k)
    return repeats

def find_repeats(counter):
    """Makes a list of keys with values greater than 1.

    counter: dictionary that maps from keys to counts

    returns: list of keys
    """
    return [k for k,v in counter.items() if v > 1]

if __name__ == '__main__':
    print(
        find_repeats_v1(
            value_counts_efficient('hello')))
    print('-'*80)
    print(
        find_repeats(
            value_counts_efficient('hello')))