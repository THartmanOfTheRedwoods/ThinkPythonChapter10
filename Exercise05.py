#!/usr/bin/env python3

from Exercise02 import value_counts_efficient

def add_counters_v1(counter1, counter2):
    result = dict(counter1)
    for k, v in counter2.items():
        result[k] = result.get(k, 0) + v
    return result

def add_counters(counter1, counter2):
    return {k: counter1.get(k, 0) + counter2.get(k, 0)
            for k in set(counter1.keys()).union(set(counter2.keys()))}

if __name__ == '__main__':
    print(add_counters_v1(
        value_counts_efficient('brontosaurus'),
        value_counts_efficient('apatosaurus')
    ))
    print('-'*80)
    print(add_counters(
        value_counts_efficient('brontosaurus'),
        value_counts_efficient('apatosaurus')
    ))