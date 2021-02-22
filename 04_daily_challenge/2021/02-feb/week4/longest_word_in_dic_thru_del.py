# https://leetcode.com/explore/challenge/card/february-leetcoding-challenge-2021/587/week-4-february-22nd-february-28th/3649/

# Longest Word in Dictionary through Deleting
#
# Given a string and a string dictionary, find the longest string in the
# dictionary that can be formed by deleting some characters of the given
# string. If there are more than one possible results, return the longest word
# with the smallest lexicographical order. If there is no possible result,
# return the empty string.

# Example 1:
# Input:
# s = "abpcplea", d = ["ale","apple","monkey","plea"]
# Output:
# "apple"

# Example 2:
# Input:
# s = "abpcplea", d = ["a","b","c"]
# Output:
# "a"

# Note:
# All the strings in the input will only contain lower-case letters.
# The size of the dictionary won't exceed 1,000.
# The length of all the strings in the input won't exceed 1,000.

# amazing python solutions and code
# https://leetcode.com/problems/longest-word-in-dictionary-through-deleting/discuss/99590/Short-Python-solutions

from typing import Callable, List
from termcolor import colored

import heapq


class Solution:
    def findLongestWord(self, s: str, d: List[str]) -> str:
        return self.findLongestWord_sort(s, d)

    def findLongestWord_fast_optimized_sort(self, s: str, d: List[str]) -> str:
        for word in sorted(d, key=lambda x: (-len(x), x)):
            it = iter(s)
            if all(c in it for c in word):
                return word
        return ""

    def findLongestWord_min_sort_using_heap(self, s: str, d: List[str]) -> str:
        heap = [(-len(word), word) for word in d]
        heapq.heapify(heap)
        while heap:
            word = heapq.heappop(heap)[1]
            it = iter(s)
            if all(c in it for c in word):
                return word
        return ""

    def findLongestWord_sort(self, s: str, d: List[str]) -> str:
        n = len(s)
        if n == 0:
            return ""
        res = ""
        d.sort(reverse=True, key=lambda x: len(x))
        for word in d:
            i, j, wn = 0, 0, len(word)
            if wn > n:
                continue
            if wn < len(res):
                break
            while i < n and j < wn:
                if s[i] != word[j]:
                    i += 1
                else:
                    i += 1
                    j += 1
            if j == wn:
                if wn > len(res) or (wn == len(res) and word < res):
                    res = word
        return res


SolutionFunc = Callable[[str, List[str]], str]


def test_solution(s: str, d: List[str], expected: str) -> None:
    def test_impl(func: SolutionFunc, s: str, d: List[str], expected: str) -> None:
        r = func(s, d)
        if r == expected:
            print(
                colored(
                    f"PASSED {func.__name__} => longest word in {d} by deleting char in {s} is {r}",
                    "green",
                )
            )
        else:
            print(
                colored(
                    f"FAILED {func.__name__} => longest word in {d} by deleting char in {s} is {r}, but expected {expected}",
                    "red",
                )
            )

    sln = Solution()
    test_impl(sln.findLongestWord_sort, s, d, expected)
    test_impl(sln.findLongestWord_fast_optimized_sort, s, d, expected)
    test_impl(sln.findLongestWord_min_sort_using_heap, s, d, expected)


if __name__ == "__main__":
    test_solution(s="abpcplea", d=["ale", "apple", "monkey", "plea"], expected="apple")
    test_solution(s="abpcplea", d=["a", "b", "c"], expected="a")
    test_solution(s="fuzz", d=["a", "b", "c"], expected="")
