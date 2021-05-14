# https://leetcode.com/explore/challenge/card/may-leetcoding-challenge-2021/599/week-2-may-8th-may-14th/3741/

# Ambiguous Coordinates
# We had some 2-dimensional coordinates, like "(1, 3)" or "(2, 0.5)".  Then, we
# removed all commas, decimal points, and spaces, and ended up with the string
# s.  Return a list of strings representing all possibilities for what our
# original coordinates could have been.

# Our original representation never had extraneous zeroes, so we never started
# with numbers like "00", "0.0", "0.00", "1.0", "001", "00.01", or any other
# number that can be represented with less digits.  Also, a decimal point
# within a number never occurs without at least one digit occuring before it,
# so we never started with numbers like ".1".

# The final answer list can be returned in any order.  Also note that all
# coordinates in the final answer have exactly one space between them
# (occurring after the comma.)

# Example 1:
# Input: s = "(123)"
# Output: ["(1, 23)", "(12, 3)", "(1.2, 3)", "(1, 2.3)"]

# Example 2:
# Input: s = "(00011)"
# Output:  ["(0.001, 1)", "(0, 0.011)"]
# Explanation:
# 0.0, 00, 0001 or 00.01 are not allowed.

# Example 3:
# Input: s = "(0123)"
# Output: ["(0, 123)", "(0, 12.3)", "(0, 1.23)", "(0.1, 23)", "(0.1, 2.3)",
# "(0.12, 3)"]

# Example 4:
# Input: s = "(100)"
# Output: [(10, 0)]
# Explanation:
# 1.0 is not allowed.

# Note:
# 4 <= s.length <= 12.
# s[0] = "(", s[s.length - 1] = ")", and the other elements in s are digits.

from typing import Callable, List
from termcolor import colored
from itertools import product


class Solution:
    # https://leetcode.com/problems/ambiguous-coordinates/discuss/123851/C%2B%2BJavaPython-Solution-with-Explanation
    def ambiguousCoordinates(self, s: str) -> List[str]:
        s = s[1:-1]

        def f(s: str) -> List[str]:
            if not s or len(s) > 1 and s[0] == s[-1] == "0":
                return []
            if s[-1] == "0":
                return [s]
            if s[0] == "0":
                return [s[0] + "." + s[1:]]
            return [s] + [s[:i] + "." + s[i:] for i in range(1, len(s))]

        return [
            f"({a}, {b})" for i in range(len(s)) for a, b in product(f(s[:i]), f(s[i:]))
        ]


SolutionFunc = Callable[[str], List[str]]


def test_solution(s: str, expected: List[str]) -> None:
    def test_impl(func: SolutionFunc, s: str, expected: List[str]) -> None:
        r = func(s)
        if sorted(r) == sorted(expected):
            print(
                colored(
                    f"PASSED {func.__name__} => Coordinates from {s} are {r}", "green"
                )
            )
        else:
            print(
                colored(
                    f"FAILED {func.__name__} => Coordinates from {s} are {r} but expected {expected}",
                    "red",
                )
            )

    sln = Solution()
    test_impl(sln.ambiguousCoordinates, s, expected)


if __name__ == "__main__":
    test_solution(s="(12)", expected=["(1, 2)"])
    test_solution(s="(123)", expected=["(1, 23)", "(12, 3)", "(1.2, 3)", "(1, 2.3)"])
    test_solution(s="(00011)", expected=["(0.001, 1)", "(0, 0.011)"])
    test_solution(
        s="(0123)",
        expected=[
            "(0, 123)",
            "(0, 12.3)",
            "(0, 1.23)",
            "(0.1, 23)",
            "(0.1, 2.3)",
            "(0.12, 3)",
        ],
    )
    test_solution(s="(100)", expected=["(10, 0)"])
