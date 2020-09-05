from typing import List
from collections import defaultdict


class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        bank, path, queue = defaultdict(list), {beginWord}, [(beginWord, 1)]

        length = len(beginWord)
        for word in wordList:
            for i in range(length):
                bank[word[:i] + "*" + word[i + 1 :]].append(word)

        while queue:
            cur_word, level = queue.pop(0)
            for i in range(length):
                temp_word = cur_word[:i] + "*" + cur_word[i + 1 :]
                for w in bank[temp_word]:
                    if w == endWord:
                        return level + 1
                    if w not in path:
                        path.add(w)
                        queue.append((w, level + 1))
            bank[cur_word] = []
        return 0