# https://leetcode.com/explore/challenge/card/april-leetcoding-challenge-2021/596/week-4-april-22nd-april-28th/3718/

# Count Binary Substrings
# Give a string s, count the number of non-empty (contiguous) substrings that
# have the same number of 0's and 1's, and all the 0's and all the 1's in these
# substrings are grouped consecutively.

# Substrings that occur multiple times are counted the number of times they occur.

# Example 1:
# Input: "00110011"
# Output: 6
# Explanation: There are 6 substrings that have equal number of consecutive 1's
# and 0's: "0011", "01", "1100", "10", "0011", and "01".


# Notice that some of these substrings repeat and are counted the number of
# times they occur.
# Also, "00110011" is not a valid substring because all the 0's (and 1's) are
# not grouped together.

# Example 2:
# Input: "10101"
# Output: 4
# Explanation: There are 4 substrings: "10", "01", "10", "01" that have equal
# number of consecutive 1's and 0's.

# Note:
# s.length will be between 1 and 50,000.
# s will only consist of "0" or "1" characters.


from typing import Callable, List
from termcolor import colored


class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        return self.countBinarySubstrings_pythonic(s)

    def countBinarySubstrings_pythonic(self, s: str) -> int:
        m: List[int] = list(
            map(len, s.replace("01", "0 1").replace("10", "1 0").split())
        )
        return sum(min(a, b) for a, b in zip(m, m[1:]))


SolutionFunc = Callable[[str], int]


def test_solution(s: str, expected: int) -> None:
    def test_impl(func: SolutionFunc, s: str, expected: int) -> None:
        r = func(s)
        if r == expected:
            print(
                colored(
                    f"PASSED {func.__name__} => Number of non-empty substrings from {s} is {r}",
                    "green",
                )
            )
        else:
            print(
                colored(
                    f"FAILED {func.__name__} => Number of non-empty substrings from {s} is {r}, but expected {expected}",
                    "red",
                )
            )

    sln = Solution()
    test_impl(sln.countBinarySubstrings, s, expected)


if __name__ == "__main__":
    test_solution(s="00110011", expected=6)
    test_solution(s="10101", expected=4)
