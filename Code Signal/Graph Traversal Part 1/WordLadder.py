"""
Given two words, beginWord and endWord, and a wordList of approved words, find the length of the shortest transformation sequence from beginWord to endWord such that:

Only one letter can be changed at a time
Each transformed word must exist in the wordList.
The length of the sequence is defined as the number of words in it, e.g. the length of "cot" -> "hot" -> "hit" is 3, and the length of "dog" -> "cog" is 2.

Return the length of the shortest transformation sequence, or 0 if no such transformation sequence exists.

Note: beginWord does not count as a transformed word. You can assume that beginWord and endWord are not empty and are not the same.

Example

For beginWord = "hit", endWord = "cog", and wordList = ["hot", "dot", "dog", "lot", "log", "cog"], the output should be
wordLadder(beginWord, endWord, wordList) = 5.

The shortest transformation is "hit" -> "hot" -> "dot" -> "dog" -> "cog" with a length of 5.

For beginWord = "a", endWord = "c", and wordList = ["a", "b", "c"], the output should be
wordLadder(beginWord, endWord, wordList) = 2.

It is possible to obtain endWord = "c" from beginWord = "a" without using any additional words in the middle: "a" -> "c".
"""
from collections import deque

def wordLadder(beginWord, endWord, wordList):
    wordList = set(wordList)
    queue = deque([[beginWord, 1]])
    while queue:
        word, length = queue.popleft()
        if word == endWord:
            return length
        for i in range(len(word)):
            for c in 'abcdefghijklmnopqrstuvwxyz':
                next_word = word[:i] + c + word[i+1:]
                if next_word in wordList:
                    wordList.remove(next_word)
                    queue.append([next_word, length + 1])
    return 0