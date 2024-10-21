#!/usr/bin/env python3

from Exercise02 import value_counts_efficient

def has_duplicates_efficient(word):
    return len(set(word)) < len(word)

def has_duplicates_comprehension(word):
    return any(v > 1 for v in dict.values(value_counts_efficient( word )))

def has_duplicates(word):
    counter = value_counts_efficient(word)
    for k,v in counter.items():
        if v > 1:
            return True
    return False

if __name__ == '__main__':
    print(has_duplicates('un-unpredictably'))
    print(has_duplicates('unpredictably'))
    print('-'* 80)
    print(has_duplicates_comprehension('un-unpredictably'))
    print(has_duplicates_comprehension('unpredictably'))
    print('-'* 80)
    print(has_duplicates_efficient('un-unpredictably'))
    print(has_duplicates_efficient('unpredictably'))