# https://leetcode.com/explore/challenge/card/june-leetcoding-challenge-2021/606/week-4-june-22nd-june-28th/3788/

# Number of Matching Subsequences
# Given a string s and an array of strings words, return the number of words[i]
# that is a subsequence of s.

# A subsequence of a string is a new string generated from the original string
# with some characters (can be none) deleted without changing the relative
# order of the remaining characters.

# For example, "ace" is a subsequence of "abcde".

# Example 1:
# Input: s = "abcde", words = ["a","bb","acd","ace"]
# Output: 3
# Explanation: There are three strings in words that are a subsequence of s:
# "a", "acd", "ace".

# Example 2:
# Input: s = "dsahjpjauf", words = ["ahjpjau","ja","ahbwzgqnuk","tnmlanowax"]
# Output: 2

# Constraints:

# 1 <= s.length <= 5 * 10⁴
# 1 <= words.length <= 5000
# 1 <= words[i].length <= 50
# s and words[i] consist of only lowercase English letters.

from bisect import bisect_left
from typing import Callable, Counter, DefaultDict, Iterator, List, Optional

from termcolor import colored


class Solution:
    # Time complexity: O(N * K^2)
    def numMatchingSubseq_brute_force(self, s: str, words: List[str]) -> int:
        def is_subsequence(w: str, s: str) -> bool:
            if len(w) > len(s):
                return False
            if w == s:
                return True
            i = 0
            for c in s:
                if i >= len(w):
                    return False
                if w[i] == c:
                    i += 1
                    if i == len(w) - 1:
                        return True
            return False

        res = 0
        for w in words:
            if is_subsequence(w, s):
                res += 1
        return res

    # let K be max length of word in words, N be number of words
    # Time complexity:   O(N + logK) => O(N) to build default dict, logK for
    # binary search
    # Space complexity: O(N) for dictionary
    def numMatchingSubseq_binary_search_dict(self, s: str, words: List[str]) -> int:
        def is_match(w: str, w_i: int, d_i: int) -> int:
            if w_i == len(w):
                return True
            lst = dic[w[w_i]]
            if len(lst) == 0 or d_i > lst[-1]:
                return False
            i = lst[bisect_left(lst, d_i)]
            return is_match(w, w_i + 1, i + 1)

        dic = DefaultDict[str, List[int]](list)
        for i, c in enumerate(s):
            dic[c].append(i)
        return sum(is_match(w, 0, 0) for w in words)

    # https://leetcode.com/problems/number-of-matching-subsequences/discuss/117634/Efficient-and-simple-go-through-words-in-parallel-with-explanation
    #
    # Time complexity: O(N)
    def numMatchingSubseq_iterators_1(self, s: str, words: List[str]) -> int:
        waiting = DefaultDict[Optional[str], List[Iterator[str]]](list)

        for w in words:
            waiting[w[0]].append(iter(w[1:]))

        for c in s:
            for it in waiting.pop(c, ()):
                waiting[next(it, None)].append(it)

        return len(waiting[None])

    def numMatchingSubseq_fastest(self, s: str, words: List[str]) -> int:
        count = 0
        for i, c in Counter(words).items():
            indexj = 0
            for j in i:
                indexj = s.find(j, indexj) + 1
                if not indexj:
                    break
            else:
                count += c
        return count


SolutionFunc = Callable[[str, List[str]], int]


def test_solution(s: str, words: List[str], expected: int) -> None:
    def test_impl(func: SolutionFunc, s: str, words: List[str], expected: int) -> None:
        r = func(s, words)
        if r == expected:
            print(
                colored(
                    f"PASSED {func.__name__} => Number of words in {words} that is a matching subsequence of {s} is {r}",
                    "green",
                )
            )
        else:
            print(
                colored(
                    f"FAILED {func.__name__} => Number of words in {words} that is a matching subsequence of {s} is {r} but expected {expected}",
                    "red",
                )
            )

    sln = Solution()
    test_impl(sln.numMatchingSubseq_brute_force, s, words, expected)
    test_impl(sln.numMatchingSubseq_binary_search_dict, s, words, expected)
    test_impl(sln.numMatchingSubseq_iterators_1, s, words, expected)
    test_impl(sln.numMatchingSubseq_fastest, s, words, expected)


if __name__ == "__main__":
    test_solution(s="abcde", words=["a", "bb", "acd", "ace"], expected=3)
    test_solution(
        s="dsahjpjauf", words=["ahjpjau", "ja", "ahbwzgqnuk", "tnmlanowax"], expected=2
    )
