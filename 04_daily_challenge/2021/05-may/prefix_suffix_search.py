# https://leetcode.com/explore/challenge/card/may-leetcoding-challenge-2021/598/week-1-may-1st-may-7th/3728/

# Prefix and Suffix Search
# Design a special dictionary which has some words and allows you to search the
# words in it by a prefix and a suffix.

# Implement the WordFilter class:

# WordFilter(string[] words) Initializes the object with the words in the
# dictionary.

# f(string prefix, string suffix) Returns the index of the word in the
# dictionary which has the prefix prefix and the suffix suffix. If there is
# more than one valid index, return the largest of them. If there is no such
# word in the dictionary, return -1.

# Example 1:
# Input
# ["WordFilter", "f"]
# [[["apple"]], ["a", "e"]]
# Output
# [null, 0]

# Explanation
# WordFilter wordFilter = new WordFilter(["apple"]);
# wordFilter.f("a", "e"); // return 0, because the word at index 0 has prefix =
# "a" and suffix = 'e".

# Constraints:
# 1 <= words.length <= 15000
# 1 <= words[i].length <= 10
# 1 <= prefix.length, suffix.length <= 10
# words[i], prefix and suffix consist of lower-case English letters only.
# At most 15000 calls will be made to the function f.

# https://leetcode.com/problems/prefix-and-suffix-search/discuss/1185171/Python-Two-solutions-%2B-Trie-and-bruteforce-explained

from __future__ import annotations
from typing import DefaultDict, Dict, List, Protocol, Set
from termcolor import colored


class TrieNode:
    def __init__(self) -> None:
        self.children: Dict[str, TrieNode] = {}
        self.index = 0


class Trie:
    def __init__(self) -> None:
        self.root = TrieNode()

    def insert(self, word: str, index: int) -> None:
        root = self.root
        root.index = index
        for symbol in word:
            root = root.children.setdefault(symbol, TrieNode())
            root.index = index

    def startsWith(self, word: str) -> int:
        root = self.root
        for symbol in word:
            if symbol not in root.children:
                return -1
            root = root.children[symbol]
        return root.index


class WordFilter(Protocol):
    def __init__(self, words: List[str]):
        ...

    def f(self, prefix: str, suffix: str) -> int:
        ...


class WordFilter_Merged_Trie(WordFilter):
    def __init__(self, words: List[str]):
        self.trie = Trie()
        self.words = {}

        for index, word in enumerate(words):
            long = word + "#" + word
            for i in range(len(word)):
                self.trie.insert(long[i:], index)

    def f(self, prefix: str, suffix: str) -> int:
        return self.trie.startsWith(suffix + "#" + prefix)


# Faster time complexity, 560ms
class WordFilter_Intersect_Prefix_Suffix(WordFilter):
    def __init__(self, words: List[str]):
        self.pre = DefaultDict[str, Set[int]](set)
        self.suf = DefaultDict[str, Set[int]](set)
        seen: Set[str] = set()
        for i in reversed(range(len(words))):
            w = words[i]
            if w in seen:
                continue
            seen.add(w)
            for j in range(len(w) + 1):
                self.pre[w[:j]].add(i)
                self.suf[w[j:]].add(i)

    def f(self, prefix: str, suffix: str) -> int:
        a = self.pre[prefix]
        b = self.suf[suffix]
        x = a & b
        return max(x) if x else -1


def test_solution(words: List[str], prefix: str, suffix: str, expected: int) -> None:
    def test_impl(
        word_filter: WordFilter, prefix: str, suffix: str, expected: int
    ) -> None:
        r = word_filter.f(prefix, suffix)
        if r == expected:
            print(
                colored(
                    f"PASSED {type(word_filter)}=> index of word starting with {prefix} and ending with {suffix} from {words} is {r}",
                    "green",
                )
            )
        else:
            print(
                colored(
                    f"FAILED {type(word_filter)}=> index of word starting with {prefix} and ending with {suffix} from {words} is {r}, but expected is {expected}",
                    "red",
                )
            )

    test_impl(WordFilter_Merged_Trie(words), prefix, suffix, expected)
    test_impl(WordFilter_Intersect_Prefix_Suffix(words), prefix, suffix, expected)


if __name__ == "__main__":
    test_solution(words=["apple"], prefix="a", suffix="e", expected=0)
