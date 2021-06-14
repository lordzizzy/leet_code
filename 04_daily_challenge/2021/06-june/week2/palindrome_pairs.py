# https://leetcode.com/explore/challenge/card/june-leetcoding-challenge-2021/604/week-2-june-8th-june-14th/3777/

# Palindrome Pairs

# Solution
# Given a list of unique words, return all the pairs of the distinct indices
# (i, j) in the given list, so that the concatenation of the two words words[i]
# + words[j] is a palindrome.

# Example 1:
# Input: words = ["abcd","dcba","lls","s","sssll"]
# Output: [[0,1],[1,0],[3,2],[2,4]]
# Explanation: The palindromes are ["dcbaabcd","abcddcba","slls","llssssll"]

# Example 2:
# Input: words = ["bat","tab","cat"]
# Output: [[0,1],[1,0]]
# Explanation: The palindromes are ["battab","tabbat"]

# Example 3:
# Input: words = ["a",""]
# Output: [[0,1],[1,0]]

# Constraints:
# 1 <= words.length <= 5000
# 0 <= words[i].length <= 300
# words[i] consists of lower-case English letters.

from __future__ import annotations

from typing import Callable, List, DefaultDict
from collections import defaultdict
from termcolor import colored


class TrieNode:
    def __init__(self):
        self.idx = -1
        self.pdromes_below: List[int] = []
        self.children: DefaultDict[str, TrieNode] = defaultdict(TrieNode)


class Trie:
    def __init__(self) -> None:
        self.root = TrieNode()

    def add(self, word: str, idx: int) -> None:
        node = self.root
        for i, letter in enumerate(reversed(word)):
            if self.is_palindrome(word[: len(word) - i]):
                node.pdromes_below.append(idx)
            node = node.children[letter]
        node.idx = idx

    def search(self, word: str, idx: int, res: List[List[int]]) -> List[List[int]]:
        node = self.root
        for i, letter in enumerate(word):
            if node.idx >= 0 and idx != node.idx and self.is_palindrome(word[i:]):
                res.append([idx, node.idx])
            node = node.children.get(letter)
            if not node:
                return res
        for p in node.pdromes_below:
            if p != idx:
                res.append([idx, p])
        if node.idx >= 0 and idx != node.idx:
            res.append([idx, node.idx])
        return res

    def is_palindrome(self, word: str) -> bool:
        i, j = 0, len(word) - 1
        while i < j:
            if word[i] != word[j]:
                return False
            i += 1
            j -= 1
        return True


class Solution:
    # Time complexity: O(N^2*K), Space complexity O(1)
    def palindromePairs_bruteforce(self, words: List[str]) -> List[List[int]]:
        def is_palindrome(word: str) -> bool:
            l, r = 0, len(word) - 1
            while l < r:
                if word[l] != word[r]:
                    return False
                l += 1
                r -= 1
            return True

        res: List[List[int]] = []

        for i, w1 in enumerate(words):
            for j, w2 in enumerate(words):
                if i != j:
                    if is_palindrome(w1 + w2):
                        res.append([i, j])

        return res

    # References
    # https://leetcode.com/problems/palindrome-pairs/discuss/79195/O(n-*-k2)-java-solution-with-Trie-structure
    # http://www.allenlipeng47.com/blog/index.php/2016/03/15/palindrome-pairs/
    #
    # Time complexity: O(N * K^2), Space complexity: O(N*26K^2)
    def palindromePairs_reverse_trie(self, words: List[str]) -> List[List[int]]:
        res: List[List[int]] = []
        t = Trie()
        for idx, w in enumerate(words):
            t.add(w, idx)
        for idx, w in enumerate(words):
            res = t.search(w, idx, res)
        return res


SolutionFunc = Callable[[List[str]], List[List[int]]]


def test_solution(words: List[str], expected: List[List[int]]) -> None:
    def test_impl(
        func: SolutionFunc, words: List[str], expected: List[List[int]]
    ) -> None:
        r = func(words)
        if sorted(r) == sorted(expected):
            print(
                colored(
                    f"PASSED {func.__name__} => Pairs of distinct indices in {words} is {r}",
                    "green",
                )
            )
        else:
            print(
                colored(
                    f"FAILED {func.__name__} => Pairs of distinct indices in {words} is {r} but expected {expected}",
                    "red",
                )
            )

    sln = Solution()
    test_impl(sln.palindromePairs_bruteforce, words, expected)
    test_impl(sln.palindromePairs_reverse_trie, words, expected)


if __name__ == "__main__":
    test_solution(
        words=["abcd", "dcba", "lls", "s", "sssll"],
        expected=[[0, 1], [1, 0], [3, 2], [2, 4]],
    )
    test_solution(words=["bat", "tab", "cat"], expected=[[0, 1], [1, 0]])
    test_solution(words=["a", ""], expected=[[0, 1], [1, 0]])
    test_solution(
        words=["a", "abc", "aba", ""], expected=[[0, 3], [3, 0], [2, 3], [3, 2]]
    )
