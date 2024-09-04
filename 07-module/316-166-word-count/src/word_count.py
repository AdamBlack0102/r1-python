#! /usr/bin/env python
# -*- coding: utf-8 -*-
def wordcount(filepath):
    set_words = []
    words_count = []
    length_max = 0
    fp = open(filepath, 'r')
    text = fp.read()
    line_words = (text.split())
    for word in line_words:
        length_max = max(length_max, len(word))
        if word in set_words:
            index_word = set_words.index(word)
            words_count[index_word] += 1
        else:
            set_words.append(word)
            words_count.append(0)
    words_list = list(zip(set_words, words_count))
    words_list = sorted(words_list, reverse=False, key=lambda x: (-x[1], x[0]))
    for item in words_list:
        print(item[0] + ':', end='')
        for i in range(0, (length_max - len(item[0]) + 1)):
            print(" ", end='')
        for j in range(0, item[1]+1):
            print("*", end='')
        print("\n", end='')
