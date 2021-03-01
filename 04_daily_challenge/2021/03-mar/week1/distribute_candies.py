# Distribute Candies
# Alice has n candies, where the ith candy is of type candyType[i]. Alice
# noticed that she started to gain weight, so she visited a doctor.

# The doctor advised Alice to only eat n / 2 of the candies she has (n is
# always even). Alice likes her candies very much, and she wants to eat the
# maximum number of different types of candies while still following the
# doctor's advice.

# Given the integer array candyType of length n, return the maximum number of
# different types of candies she can eat if she only eats n / 2 of them.

# Example 1:
# Input: candyType = [1,1,2,2,3,3]
# Output: 3
# Explanation: Alice can only eat 6 / 2 = 3 candies. Since there are only 3
# types, she can eat one of each type.

# Example 2:
# Input: candyType = [1,1,2,3]
# Output: 2
# Explanation: Alice can only eat 4 / 2 = 2 candies. Whether she eats types
# [1,2], [1,3], or [2,3], she still can only eat 2 different types.

# Example 3:
# Input: candyType = [6,6,6,6]
# Output: 1
# Explanation: Alice can only eat 4 / 2 = 2 candies. Even though she can eat 2
# candies, she only has 1 type.

# Constraints:
# n == candyType.length
# 2 <= n <= 10⁴
# n is even.
# -10⁵ <= candyType[i] <= 10⁵

from typing import Callable, DefaultDict, List
from termcolor import colored


class Solution:
    def distributeCandies(self, candyType: List[int]) -> int:
        return self.distributeCandies_dict(candyType)

    def distributeCandies_dict(self, candyType: List[int]) -> int:
        d = DefaultDict[int, int](lambda: 0)
        for c in candyType:
            d[c] += 1
        return min(len(d), len(candyType) // 2)

    def distributeCandies_set(self, candyType: List[int]) -> int:
        eat = len(candyType) // 2
        unique = len(set(candyType))
        return min(eat, unique)


SolutionFunc = Callable[[List[int]], int]


def test_solution(candyType: List[int], expected: int) -> None:
    def test_impl(func: SolutionFunc, candyType: List[int], expected: int) -> None:
        r = func(candyType)
        if r == expected:
            print(
                colored(
                    f"PASSED {func.__name__}=> max num of {candyType} types of candies she can eat is {r}",
                    "green",
                )
            )
        else:
            print(
                colored(
                    f"FAILED {func.__name__}=> max num of {candyType} types of candies she can eat is {r} but expected {expected}",
                    "red",
                )
            )

    sln = Solution()
    test_impl(sln.distributeCandies_dict, candyType, expected)
    test_impl(sln.distributeCandies_set, candyType, expected)


if __name__ == "__main__":
    test_solution(candyType=[1, 1, 2, 2, 3, 3], expected=3)
    test_solution(candyType=[1, 1, 2, 3], expected=2)
    test_solution(candyType=[6, 6, 6, 6], expected=1)
