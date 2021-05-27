# https://leetcode.com/explore/challenge/card/may-leetcoding-challenge-2021/601/week-4-may-22nd-may-28th/3757/

# Maximum Product of Word Lengths
# Given a string array words, return the maximum value of length(word[i]) *
# length(word[j]) where the two words do not share common letters. If no such
# two words exist, return 0.

# Example 1:
# Input: words = ["abcw","baz","foo","bar","xtfn","abcdef"]
# Output: 16
# Explanation: The two words can be "abcw", "xtfn".

# Example 2:
# Input: words = ["a","ab","abc","d","cd","bcd","abcd"]
# Output: 4
# Explanation: The two words can be "ab", "cd".

# Example 3:
# Input: words = ["a","aa","aaa","aaaa"]
# Output: 0
# Explanation: No such pair of words.

# Constraints:
# 2 <= words.length <= 1000
# 1 <= words[i].length <= 1000
# words[i] consists only of lowercase English letters.

from typing import Callable, Dict, List
from termcolor import colored
from itertools import combinations


class Solution:
    def maxProduct(self, words: List[str]) -> int:
        return self.maxProduct_first(words)

    # my slow first attempt
    def maxProduct_first(self, words: List[str]) -> int:
        ans = 0
        for i, w1 in enumerate(words):
            set1 = set(w1)
            min_len = ans // len(w1) + 1
            for w2 in words[i + 1 :]:
                if len(w2) < min_len:
                    continue
                if any(c in set1 for c in w2):
                    continue
                ans = max(ans, len(w1) * len(w2))
        return ans

    # using bit-masking, each char as 1 bit, set to 1 if exist
    # enough for 26-letters, since int is at least 32 bits
    def maxProduct_bitmasking(self, words: List[str]) -> int:
        d: Dict[int, int] = {}
        for w in words:
            mask = 0
            for c in set(w):
                mask |= 1 << (ord(c) - 97)
            d[mask] = max(d.get(mask, 0), len(w))
        return max(
            [d[m1] * d[m2] for m1, m2 in combinations(d.keys(), 2) if not m1 & m2]
            or [0]
        )


SolutionFunc = Callable[[List[str]], int]


def test_solution(words: List[str], expected: int) -> None:
    def test_impl(func: SolutionFunc, words: List[str], expected: int) -> None:
        r = func(words)
        if r == expected:
            print(
                colored(
                    f"PASSED {func.__name__} => Maximum product of word lengths of {words} is {r}",
                    "green",
                )
            )
        else:
            print(
                colored(
                    f"FAILED {func.__name__} => Maximum product of word lengths of {words} is {r} but expected {expected}",
                    "red",
                )
            )

    sln = Solution()
    test_impl(sln.maxProduct_first, words, expected)
    test_impl(sln.maxProduct_bitmasking, words, expected)


if __name__ == "__main__":
    test_solution(words=["abcw", "baz", "foo", "bar", "xtfn", "abcdef"], expected=16)
    test_solution(words=["a", "ab", "abc", "d", "cd", "bcd", "abcd"], expected=4)
    test_solution(words=["a", "aa", "aaa", "aaaa"], expected=0)
