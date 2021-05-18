# https://leetcode.com/explore/challenge/card/may-leetcoding-challenge-2021/600/week-3-may-15th-may-21st/3746/

# Longest String Chain
# Given a list of words, each word consists of English lowercase letters.

# Let's say word1 is a predecessor of word2 if and only if we can add exactly
# one letter anywhere in word1 to make it equal to word2. For example, "abc" is
# a predecessor of "abac".

# A word chain is a sequence of words [word_1, word_2, ..., word_k] with k >=
# 1, where word_1 is a predecessor of word_2, word_2 is a predecessor of
# word_3, and so on.

# Return the longest possible length of a word chain with words chosen from the
# given list of words.

# Example 1:
# Input: words = ["a","b","ba","bca","bda","bdca"]
# Output: 4
# Explanation: One of the longest word chain is "a","ba","bda","bdca".

# Example 2:
# Input: words = ["xbc","pcxbcf","xb","cxbc","pcxbc"]
# Output: 5

# Constraints:
# 1 <= words.length <= 1000
# 1 <= words[i].length <= 16
# words[i] only consists of English lowercase letters.

from typing import Callable, Dict, List
from termcolor import colored


class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        return self.longestStrChain_topdown_dp_memoization(words)

    def longestStrChain_topdown_dp_memoization(self, words: List[str]) -> int:
        word_set = set(words)
        dic: Dict[str, int] = {}

        def dfs(word: str) -> int:
            if word in dic:
                return dic[word]
            max_len = 1
            for i in range(len(word)):
                sub = word[0:i] + word[i + 1 :]
                if sub in word_set:
                    max_len = max(max_len, 1 + dfs(sub))

            dic[word] = max_len
            return max_len

        ans = 0
        for w in words:
            ans = max(ans, dfs(w))
        return ans

    # https://leetcode.com/problems/longest-string-chain/discuss/294890/JavaC%2B%2BPython-DP-Solution
    def longestStrChain_bottomup_dp_sorted(self, words: List[str]) -> int:
        dp: Dict[str, int] = {}
        for w in sorted(words, key=len):
            dp[w] = max(dp.get(w[:i] + w[i + 1 :], 0) + 1 for i in range(len(w)))
        return max(dp.values())


SolutionFunc = Callable[[List[str]], int]


def test_solution(words: List[str], expected: int) -> None:
    def test_impl(func: SolutionFunc, words: List[str], expected: int) -> None:
        r = func(words)
        if r == expected:
            print(
                colored(
                    f"PASSED {func.__name__} => Longest length of word chain from {words} is {r}",
                    "green",
                )
            )
        else:
            print(
                colored(
                    f"FAILED {func.__name__} => Longest length of word chain from {words} is {r} but expected {expected}",
                    "red",
                )
            )

    sln = Solution()
    test_impl(sln.longestStrChain_topdown_dp_memoization, words, expected)
    test_impl(sln.longestStrChain_bottomup_dp_sorted, words, expected)


if __name__ == "__main__":
    test_solution(words=["a", "b", "ba", "bca", "bda", "bdca"], expected=4)
    test_solution(words=["xbc", "pcxbcf", "xb", "cxbc", "pcxbc"], expected=5)
