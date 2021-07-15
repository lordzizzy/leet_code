# https://leetcode.com/explore/challenge/card/july-leetcoding-challenge-2021/609/week-2-july-8th-july-14th/3813/

# Custom Sort String
# order and str are strings composed of lowercase letters. In order, no letter
# occurs more than once.

# order was sorted in some custom order previously. We want to permute the
# characters of str so that they match the order that order was sorted. More
# specifically, if x occurs before y in order, then x should occur before y in
# the returned string.

# Return any permutation of str (as a string) that satisfies this property.

# Example:
# Input:
# order = "cba"
# str = "abcd"
# Output: "cbad"
# Explanation:
# "a", "b", "c" appear in order, so the order of "a", "b", "c" should be "c", "b", and "a".
# Since "d" does not appear in order, it can be at any position in the returned
# string. "dcba", "cdba", "cbda" are also valid outputs.


# Note:

# order has length at most 26, and no character is repeated in order.
# str has length at most 200.
# order and str consist of lowercase letters only.

from typing import Callable, Counter

from termcolor import colored


class Solution:
    # Time complexity: O(N+26)
    # Space complexity: O(26)
    def customSortString_counter(self, order: str, s: str) -> str:
        counter, ans = Counter(s), ""
        for c in order:
            if c in counter:
                ans += c * counter[c]
                counter.pop(c)

        return ans + "".join(c * counter[c] for c in counter)


SolutionFunc = Callable[[str, str], str]


def test_solution(order: str, s: str, expected: str) -> None:
    def test_impl(func: SolutionFunc, order: str, s: str, expected: str) -> None:
        r = func(order, s)
        if r == expected:
            print(
                colored(
                    f"PASSED {func.__name__} => Sorted string: {s} using order string: {order} is {r}",
                    "green",
                )
            )
        else:
            print(
                colored(
                    f"FAILED {func.__name__} => Sorted string: {s} using order string: {order} is {r} but expected {expected}",
                    "red",
                )
            )

    sln = Solution()
    test_impl(sln.customSortString_counter, order, s, expected)


if __name__ == "__main__":
    test_solution(order="cba", s="abcd", expected="cbad")
