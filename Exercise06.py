#!/usr/bin/env python3

def load_word_list(file_path):
    word_list = {}
    with open(file_path, 'r') as word_file:
        for word in word_file:
            word_list[word.strip().lower()] = True
    return word_list

def is_interlocking(word, word_list={}):
    word = word.lower()
    intword1 = word[0::2]
    intword2 = word[1::2]
    return intword1 in word_list and intword2 in word_list

if __name__ == '__main__':
    # print(is_interlocking('schooled', load_word_list('files/words.txt')))
    # print(is_interlocking('school', load_word_list('files/words.txt')))

    word_list = load_word_list('files/words.txt')
    for word in word_list:
        if len(word) >= 8 and is_interlocking(word, word_list):
            print(f'{word}: {word[0::2]}, {word[1::2]}')

