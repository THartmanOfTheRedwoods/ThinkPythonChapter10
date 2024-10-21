#!/usr/bin/evn python3

def value_counts_efficient(word):
    counter = {}
    for l in word:
        counter[l] = counter.get(l, 0) + 1
    return counter


if __name__ == '__main__':
    print(value_counts_efficient("hello"))