# https://leetcode.com/explore/challenge/card/may-leetcoding-challenge-2021/600/week-3-may-15th-may-21st/3750/

# Find and Replace Pattern
# Given a list of strings words and a string pattern, return a list of words[i]
# that match pattern. You may return the answer in any order.

# A word matches the pattern if there exists a permutation of letters p so that
# after replacing every letter x in the pattern with p(x), we get the desired
# word.

# Recall that a permutation of letters is a bijection from letters to letters:
# every letter maps to another letter, and no two letters map to the same
# letter.

# Example 1:
# Input: words = ["abc","deq","mee","aqq","dkd","ccc"], pattern = "abb"
# Output: ["mee","aqq"]
# Explanation: "mee" matches the pattern because there is a permutation {a ->
# m, b -> e, ...}.
# "ccc" does not match the pattern because {a -> c, b -> c, ...} is not a
# permutation, since a and b map to the same letter.

# Example 2:
# Input: words = ["a","b","c"], pattern = "a"
# Output: ["a","b","c"]

# Constraints:
# 1 <= pattern.length <= 20
# 1 <= words.length <= 50
# words[i].length == pattern.length
# pattern and words[i] are lowercase English letters.

from typing import Callable, Dict, List
from termcolor import colored


class Solution:
    def findAndReplacePattern(self, words: List[str], pattern: str) -> List[str]:
        return self.findAndReplacePattern_1map(words, pattern)

    def findAndReplacePattern_1map(self, words: List[str], pattern: str) -> List[str]:
        if len(pattern) == 1:
            return words

        def match(word: str) -> bool:
            m: Dict[str, str] = {}
            for p, w in zip(pattern, word):
                if m.setdefault(p, w) != w:
                    return False
            return len(set(m.values())) == len(m.values())

        return [w for w in words if match(w)]

    # https://leetcode.com/problems/find-and-replace-pattern/discuss/161288/C%2B%2BJavaPython-Normalise-Word
    def findAndReplacePattern_normalise_word(
        self, words: List[str], pattern: str
    ) -> List[str]:
        def normalise(w: str) -> List[int]:
            m: Dict[str, int] = {}
            return [m.setdefault(c, len(m)) for c in w]

        p = normalise(pattern)
        return [w for w in words if normalise(w) == p]


SolutionFunc = Callable[[List[str], str], List[str]]


def test_solution(words: List[str], pattern: str, expected: List[str]) -> None:
    def test_impl(
        func: SolutionFunc, words: List[str], pattern: str, expected: List[str]
    ) -> None:
        r = func(words, pattern)
        if r == expected:
            print(
                colored(
                    f"PASSED {func.__name__} => {words} that matches {pattern} are {r}",
                    "green",
                )
            )
        else:
            print(
                colored(
                    f"FAILED {func.__name__} => {words} that matches {pattern} are {r} but expected {expected}",
                    "red",
                )
            )

    sln = Solution()
    test_impl(sln.findAndReplacePattern_1map, words, pattern, expected)
    test_impl(sln.findAndReplacePattern_normalise_word, words, pattern, expected)


if __name__ == "__main__":
    test_solution(
        words=["abc", "deq", "mee", "aqq", "dkd", "ccc"],
        pattern="abb",
        expected=["mee", "aqq"],
    )
    test_solution(words=["a", "b", "c"], pattern="a", expected=["a", "b", "c"])
    test_solution(
        words=["ab", "cd", "fe", "gg"], pattern="ab", expected=["ab", "cd", "fe"]
    )
