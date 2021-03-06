# https://leetcode.com/explore/challenge/card/march-leetcoding-challenge-2021/588/week-1-march-1st-march-7th/3662/

# Short Encoding of Words
# A valid encoding of an array of words is any reference string s and array of
# indices indices such that:

# words.length == indices.length
# The reference string s ends with the '#' character.
# For each index indices[i], the substring of s starting from indices[i] and up
# to (but not including) the next '#' character is equal to words[i].

# Given an array of words, return the length of the shortest reference string s
# possible of any valid encoding of words.

# Example 1:
# Input: words = ["time", "me", "bell"]
# Output: 10
# Explanation: A valid encoding would be s = "time#bell#" and indices = [0, 2, 5].
# words[0] = "time", the substring of s starting from indices[0] = 0 to the
# next '#' is underlined in "time#bell#"
# words[1] = "me", the substring of s starting from indices[1] = 2 to the next
# '#' is underlined in "time#bell#"
# words[2] = "bell", the substring of s starting from indices[2] = 5 to the
# next '#' is underlined in "time#bell#"

# Example 2:
# Input: words = ["t"]
# Output: 2
# Explanation: A valid encoding would be s = "t#" and indices = [0].

# Constraints:
# 1 <= words.length <= 2000
# 1 <= words[i].length <= 7
# words[i] consists of only lowercase letters.

from typing import Callable, List
from termcolor import colored


class Solution:
    def minimumLengthEncoding(self, words: List[str]) -> int:
        return self.minimumLengthEncoding_set_discard_suffix(words)

    def minimumLengthEncoding_set_discard_suffix(self, words: List[str]) -> int:
        good = set(words)
        for w in words:
            for k in range(1, len(w)):
                good.discard(w[k:])
        return sum(len(w) + 1 for w in good)

    def minimumLengthEncoding_trie(self, words: List[str]) -> int:
        # todo
        pass


SolutionFunc = Callable[[List[str]], int]


def test_solution(words: List[str], expected: int) -> None:
    def test_impl(func: SolutionFunc, words: List[str], expected: int) -> None:
        r = func(words)
        if r == expected:
            print(
                colored(
                    f"PASSED {func.__name__} => Length of shortest reference string for {words} is {r}",
                    "green",
                )
            )
        else:
            print(
                colored(
                    f"FAILED {func.__name__} => Length of shortest reference string for {words} is {r} but expected {expected}",
                    "red",
                )
            )

    sln = Solution()
    test_impl(sln.minimumLengthEncoding_set_discard_suffix, words, expected)


if __name__ == "__main__":
    # test_solution(words=["time", "me", "bell"], expected=10)
    # test_solution(words=["t"], expected=2)
    test_solution(words=["feipyxx", "e"], expected=10)
