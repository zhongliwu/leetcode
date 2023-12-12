# -*- coding: utf-8 -*-

import collections
from typing import (
    List,
)


def ladderLength(beginWord: str, endWord: str, wordList: List[str]) -> int:
    queue = collections.deque()
    queue.append(beginWord)
    iterated = set()
    counter = 0
    while len(queue) > 0:
        next_queue = collections.deque()
        counter += 1
        for i in range(len(queue)):
            cur_ladder = queue.popleft()
            if cur_ladder == endWord:
                return counter

            iterated.add(cur_ladder)
            for elem in wordList:
                if elem in iterated:
                    continue
                if get_str_diff(cur_ladder, elem):
                    next_queue.append(elem)

        queue = next_queue

    return 0


def get_str_diff(str1: str, str2: str) -> bool:
    num_of_diff = 0
    for i in range(0, len(str1)):
        if (str1[i] != str2[i]) and (num_of_diff == 0):
            num_of_diff += 1
        elif str1[i] != str2[i]:
            return False

    return num_of_diff != 0


class Solution:
    """
    @param: start: a string
    @param: end: a string
    @param: dict: a set of string
    @return: An integer
    """

    def ladderLength(self, start, end, dict):
        dict.add(end)
        queue = collections.deque([start])
        visited = set([start])

        distance = 0
        while queue:
            distance += 1
            for i in range(len(queue)):
                word = queue.popleft()
                if word == end:
                    return distance

                for next_word in self.get_next_words(word):
                    if next_word not in dict or next_word in visited:
                        continue
                    queue.append(next_word)
                    visited.add(next_word)

        return 0

    # O(26 * L^2)
    # L is the length of word
    def get_next_words(self, word):
        words = []
        for i in range(len(word)):
            left, right = word[:i], word[i + 1:]
            for char in 'abcdefghijklmnopqrstuvwxyz':
                if word[i] == char:
                    continue
                words.append(left + char + right)
        return words